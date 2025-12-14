import uuid
from typing import Optional

from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import OpenMetadataConnection, AuthProvider
from metadata.generated.schema.entity.data.table import Table, Column, DataType
from metadata.generated.schema.api.data.createTable import CreateTableRequest
from metadata.generated.schema.api.services.createDatabaseService import CreateDatabaseServiceRequest
from metadata.generated.schema.entity.services.databaseService import DatabaseServiceType
from metadata.generated.schema.api.data.createDatabase import CreateDatabaseRequest
from metadata.generated.schema.api.data.createDatabaseSchema import CreateDatabaseSchemaRequest

from metadata.generated.schema.entity.services.connections.database.mysqlConnection import MysqlConnection

# ==========================================
# 設定
# ==========================================
SERVER_HOST = "http://localhost:8585/api"
JWT_TOKEN = "eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6InNhbXBsZSIsInJvbGVzIjpbXSwiZW1haWwiOiJzYW1wbGVAb3Blbi1tZXRhZGF0YS5vcmciLCJpc0JvdCI6dHJ1ZSwidG9rZW5UeXBlIjoiQk9UIiwiaWF0IjoxNzY1Njk5ODM3LCJleHAiOjE3NjgyOTE4Mzd9.dqmvycrh2W4mvMTiATwbHTVtLGYqLQkVcbnyL-ZO2pZLKJPazAZ-ET9O3kK7LIKbpFwaQjhSLlQUFZUBWmPlUTOp6Px-mhHW0SdQ7lZsRmIt7ZFRoPuZHxHQDTMWO2DlT4L1Le5A3Okfhyu-aPOjJ7VrO30yxZ-ld-HPBwGI9KBBIcNwYCXquYQqEDAJoNS7Q1l3p7aIHHb0lScu0Zh583nRaC0G0hpN7PJs5SU_H_ub4zFSyNMH4Z_EanpYCmr-Zg6zCwm8mTE0iY_Gd23QOrrr4BOprorAWn85DapDeM52fUOroHZz2eyzZhM2iWrJiIOW_PbhJyI-muMQV_tczg"
# ==========================================

class CatalogManager:
    def __init__(self):
        server_config = OpenMetadataConnection(
            hostPort=SERVER_HOST,
            authProvider=AuthProvider.openmetadata,
            securityConfig=OpenMetadataJWTClientConfig(jwtToken=JWT_TOKEN),
        )
        self.metadata = OpenMetadata(server_config)

        self.service_name = "test_service_mysql"
        self.db_name = "test_db"
        self.schema_name = "test_schema"
        self._prepare_hierarchy()

    def _prepare_hierarchy(self):
        """テーブルを作るための親階層（Service -> DB -> Schema）を作成"""

        mysql_config = MysqlConnection(
            type="Mysql",
            scheme="mysql+pymysql",
            username="root",
            authType={"password": "password"},
            hostPort="mysql:3306"
        )

        # 1. Create Service
        print(f"--- サービス作成: {self.service_name} ---")
        service_req = CreateDatabaseServiceRequest(
            name=self.service_name,
            serviceType=DatabaseServiceType.Mysql,
            connection={
                "config": mysql_config.model_dump()
            }
        )
        self.metadata.create_or_update(service_req)

        # 2. Create Database
        print(f"--- データベース作成: {self.db_name} ---")
        db_req = CreateDatabaseRequest(
            name=self.db_name,
            service=self.service_name
        )
        self.metadata.create_or_update(db_req)

        # 3. Create Schema
        print(f"--- スキーマ作成: {self.schema_name} ---")
        schema_req = CreateDatabaseSchemaRequest(
            name=self.schema_name,
            database=f"{self.service_name}.{self.db_name}"
        )
        self.metadata.create_or_update(schema_req)

    def register_catalog(self, name: str, description: str, category_tag: str):
        """カタログ（テーブル）を登録する"""
        create_table = CreateTableRequest(
            name=name,
            databaseSchema=f"{self.service_name}.{self.db_name}.{self.schema_name}",
            columns=[Column(name="id", dataType=DataType.INT, description="Primary Key")],
            description=description,
        )

        entity = self.metadata.create_or_update(create_table)
        print(f"[登録] カタログ '{name}' を登録しました。ID: {entity.id.root}")
        return entity

    def get_catalog(self, name: str) -> Optional[Table]:
        """カタログ（テーブル）を取得する"""
        table_fqn = f"{self.service_name}.{self.db_name}.{self.schema_name}.{name}"
        entity = self.metadata.get_by_name(entity=Table, fqn=table_fqn)

        if entity:
            desc = entity.description.root if entity.description else "No Description"
            print(f"[取得] カタログ '{name}' を取得しました。説明: {desc}")
        else:
            print(f"[エラー] カタログ '{name}' が見つかりません。")

        return entity

# ==========================================
# ロジック分岐
# ==========================================
def process_data_logic(catalog_entity: Table):
    if catalog_entity.description:
        description = catalog_entity.description.root
    else:
        description = ""

    entity_name = catalog_entity.name.root

    print(f"\n--- ロジック実行開始: {entity_name} ---")

    if "区分:機密" in description:
        print(f"🔒【高セキュリティモード】で処理します。")
        print(f"   データ '{entity_name}' は暗号化して転送されます。")
    elif "区分:公開" in description:
        print(f"🌍【公開モード】で処理します。")
        print(f"   データ '{entity_name}' はそのままAPIで公開されます。")
    else:
        print(f"⚙️【標準モード】で処理します。")

    print("--- ロジック実行終了 ---\n")


# ==========================================
# メイン処理実行
# ==========================================
if __name__ == "__main__":
    try:
        manager = CatalogManager()

        # １．カタログAを登録
        catalog_a_name = "catalog_A_secure"
        manager.register_catalog(
            name=catalog_a_name,
            description="顧客個人情報を含むデータ。区分:機密",
            category_tag="Confidential"
        )

        # ２．カタログAを取得
        entity_a = manager.get_catalog(catalog_a_name)

        # ３．カタログBを登録
        catalog_b_name = "catalog_B_public"
        manager.register_catalog(
            name=catalog_b_name,
            description="一般公開用の製品リスト。区分:公開",
            category_tag="Public"
        )

        # ４．カタログBを取得
        entity_b = manager.get_catalog(catalog_b_name)

        # ５．ロジック切り替え
        print("==========================================")
        print("同じ関数 process_data_logic に異なるカタログを渡します")
        print("==========================================")

        if entity_a:
            process_data_logic(entity_a)

        if entity_b:
            process_data_logic(entity_b)

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n[Error] 実行中にエラーが発生しました: {e}")