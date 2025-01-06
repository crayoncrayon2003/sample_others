package com.example;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.InputStream;

public class HttpServerExample {

    private static final String DEFAULT_HOST = "0.0.0.0";
    private static final int DEFAULT_PORT = 8080;
    private static Map<Integer, Integer> data = new HashMap<>();

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(DEFAULT_HOST, DEFAULT_PORT), 0);
        server.createContext("/hello", new HelloHandler());
        server.createContext("/data-api", new DataHandler());
        server.setExecutor(null);
        server.start();
        System.out.println("Server started on port " + DEFAULT_PORT);
    }

    static class HelloHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "hello\n";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }

    static class DataHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String method = exchange.getRequestMethod();
            if ("GET".equalsIgnoreCase(method)) {
                handleGet(exchange);
            } else if ("POST".equalsIgnoreCase(method)) {
                handlePost(exchange);
            }
        }

        private void handleGet(HttpExchange exchange) throws IOException {
            String query = exchange.getRequestURI().getQuery();
            int id = Integer.parseInt(query.split("=")[1]);
            String response;

            if (!data.containsKey(id)) {
                response = "{\"message\": \"id not found\", \"id\": " + id + "}";
                exchange.sendResponseHeaders(404, response.length());
            } else {
                response = "{\"id\": " + id + ", \"value\": \"" + data.get(id) + "\"}";
                exchange.sendResponseHeaders(200, response.length());
            }

            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }

        private void handlePost(HttpExchange exchange) throws IOException {
            InputStream is = exchange.getRequestBody();
            ObjectMapper objectMapper = new ObjectMapper();
            Map<String, Object> body = objectMapper.readValue(is, Map.class);
            String response;

            if (!body.containsKey("id") || !body.containsKey("value")) {
                response = "{\"message\": \"key error\", \"data\": " + body + "}";
                exchange.sendResponseHeaders(404, response.length());
            } else {
                int id = (Integer) body.get("id");
                Integer value = (Integer) body.get("value");
                data.put(id, value);
                response = "{\"message\": \"Data created\", \"id\": " + id + ", \"value\": \"" + value + "\"}";
                exchange.sendResponseHeaders(200, response.length());
            }

            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
