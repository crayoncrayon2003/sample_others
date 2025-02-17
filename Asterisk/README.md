# reference
* https://github.com/asterisk/asterisk
* https://it-kizaki-maruo.com/asterisk-install-to-ubuntu/

# Preparations
## ubuntu
'''
sudo add-apt-repository universe
sudo apt -y install git curl wget libnewt-dev libssl-dev libncurses5-dev subversion 
sudo apt -y install libsqlite3-dev build-essential libjansson-dev libxml2-dev uuid-dev
sudo apt -y install lua5.3 lua5.3-dev
'''

## asterisk
### main 
'''
cd /tmp
wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz
tar xvf asterisk-20-current.tar.gz
cd asterisk-20.4.0/
'''

### Related Modules
#### MP3
'''
contrib/scripts/get_mp3_source.sh
'''

#### ilbc codec
'''
contrib/scripts/get_ilbc_source.sh
'''

#### Confirmation before installation
'''
sudo contrib/scripts/install_prereq install
./configure
'''

# install
## select
'''
make menuselect

Codec Translators   -> codec_g**
Codec Translators   -> oupas
Core Sound Packages -> CORE-SOUNDS-JA-*
'''

## compile
'''
make
sudo make install
sudo make progdocs
sudo make samples
'''

## authorization settings
'''
sudo groupadd asterisk
sudo useradd -r -d /var/lib/asterisk -g asterisk asterisk
sudo usermod -aG audio,dialout asterisk
sudo chown -R asterisk.asterisk /etc/asterisk
sudo chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk
sudo chown -R asterisk.asterisk /usr/lib/asterisk
'''

# Startup(manual)
'''
sudo make config
ldconfig
'''

# Startup(service)
'''
sudo systemctl enable asterisk
sudo systemctl start asterisk
sudo systemctl restart asterisk
sudo systemctl status asterisk
'''

# Setting
## SIP Server and SIP Cliant
```
sudo mv /etc/asterisk/pjsip.conf /etc/asterisk/pjsip.conf.org
sudo vim /etc/asterisk/pjsip.conf
```

```
[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0

[8001]
type=endpoint
transport=transport-udp
context=default
disallow=all
allow=ulaw
auth=8001
aors=8001

[8001]
type=auth
auth_type=userpass
password=8001
username=8001

[8001]
type=aor
max_contacts=10

[8002]
type=endpoint
transport=transport-udp
context=default
disallow=all
allow=ulaw
auth=8002
aors=8002

[8002]
type=auth
auth_type=userpass
password=8002
username=8002

[8002]
type=aor
max_contacts=10

[8003]
type=endpoint
transport=transport-udp
context=default
disallow=all
allow=ulaw
auth=8003
aors=8003

[8003]
type=auth
auth_type=userpass
password=8003
username=8003

[8003]
type=aor
max_contacts=10

[8004]
type=endpoint
transport=transport-udp
;context=from-internal
context=default
disallow=all
allow=ulaw
auth=8004
aors=8004

[8004]
type=auth
auth_type=userpass
password=8004
username=8004

[8004]
type=aor
max_contacts=10
```

## Caller of SIP clients
```
sudo mv /etc/asterisk/extensions.conf /etc/asterisk/extensions.conf.org
sudo vim /etc/asterisk/extensions.conf
```

```
[general]
static=yes
writeprotect=no

;[from-internal]
;exten = 800,1,Answer()
;same = n,Wait(1)
;same = n,Playback(hello-world)
;same = n,Hangup()
;
;[8001]
;exten = 8001,1,Dial(PJSIP/8001,30,r)
;same = n.Hangup()
;
;[8002]
;exten = 8002,1,Dial(PJSIP/8002,30,r)
;same = n.Hangup()
;
;[8003]
;exten = 8003,1,Dial(PJSIP/8003,30,r)
;same = n.Hangup()
;
;[8004]
;exten = 8004,1,Dial(PJSIP/8004,30,r)
;same = n.Hangup()

[default]
exten => _80XX,1,Dial(PJSIP/${EXTEN},60,tT) ; outgoing call
exten => _80XX,n,Answer()                   ; incoming call
exten => _80XX,n,SayDigits(${EXTEN})        ; automated voice message( incoming phone number )
exten => _80XX,n,Playback(hello-world)      ; Play audio files
exten => _80XX,n,Hangup()                   ; disconnect
```

# Invoker of SIP clients
## SIP clients #8001
* Server　　　:　ip addr of asterisk
* Username　　:　8001
* Password    :  8001
* Display Name:  8001

## SIP clients #8002
* Domain　　　:　ip addr of asterisk
* Username　　:　8002
* Password    :  8002
* Display Name:  8002

# Confirm status of asterisk
```
sudo asterisk -vvvvcr
module show like sip
pjsip show endpoints
sip show peers
sip show peer　8001
```