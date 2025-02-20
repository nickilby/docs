# ClickHouse Integration Guide

---

### **Overview of the ClickHouse Setup**

**Architecture:**
- The ClickHouse cluster consists of **two nodes**: `z-click-01`, `z-click-02`.
- **ZooKeeper Cluster** (for metadata sync and quorum): `z-click-keeper-01`, `z-click-keeper-02`, `z-click-keeper-03`.
- **HAProxy** is now used as the load balancer, distributing queries to both ClickHouse nodes.
- ClickHouse nodes are set up for **internal replication** across shards.

---

### **Connecting to ClickHouse**

**Endpoints:**
- **HTTP API**: `http://clickhouse.zengenti.io:8123`
- **Native Protocol (TCP)**: `clickhouse.zengenti.io:9000`
- **Prometheus Metrics**: `[Grafana Dashboard](https://grafana.zengenti.com/d/thEkJB_Mz/clickhouse?orgId=1&refresh=30s)`

**HAProxy Configuration:**
- HAProxy is configured to balance load evenly across `z-click-01` and `z-click-02`.
- Both read and write queries should be directed to the HAProxy endpoint (`clickhouse.zengenti.io`) for optimal distribution.

**Users & Authentication:**
- **Admin User:** `admin` / `poetry-gangsta-SERBIA`

---

### **Data Ingestion**

**Kafka Integration:**
- The setup is designed to receive data from Kafka. Ensure Kafka connectors or ingestion methods align with the Kafka topics and data formats.

**FluentBit Integration:**
- Configure FluentBit to send logs directly to the HTTP API or use the native protocol for higher throughput.

---

### **Storage Policies & Data Management**

**Storage Disks:**
- **Local Disk:** `/data/clickhouse/data/`
- **S3 Disk (Minio):** `http://minio-hq2.zengenti.io:9000/click-clickhouse/`
- **Cache:** 25GB cache (`/data/clickhouse/cache/`), persistent across restarts.

**Storage Policies:**
- **Local Volume Policy:** Moves data when disk is 80% full.
- **S3 Volume Policy:** Moves parts older than 60 days to Minio.
---

### **Table Creation & Replication**

- When creating tables, ensure the table is created on all ClickHouse nodes (`z-click-01`, `z-click-02`).
- After table creation, create a **Distributed Table** to ensure data synchronization between nodes.
- Use the **production** storage policy when defining table storage to optimize performance and scalability.

Example:

```sql
CREATE DATABASE IF NOT EXISTS uk_prices;

CREATE TABLE uk_prices.price_paid
(
    transaction_id UUID,
    price UInt32,
    date_of_transfer Date,
    postcode String,
    property_type Enum8('D' = 1, 'S' = 2, 'T' = 3, 'F' = 4, 'O' = 5),
    old_new Enum8('Y' = 1, 'N' = 2),
    duration Enum8('F' = 1, 'L' = 2),
    paon String,
    saon String,
    street String,
    locality String,
    town_city String,
    district String,
    county String,
    ppd_category Enum8('A' = 1, 'B' = 2),
    record_status Enum8('A' = 1, 'C' = 2)
)
ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/uk_prices/price_paid', '{replica}')
PARTITION BY toYYYYMM(date_of_transfer)
ORDER BY (postcode, date_of_transfer)
SETTINGS storage_policy = 'production';

CREATE TABLE default.uk_price_paid AS uk_prices.price_paid
ENGINE = Distributed('clickhouse', 'uk_prices', 'price_paid', rand());

```

---

### **Querying & Load Balancing**

- **HAProxy** is the central load balancer, handling both read and write queries.
- Direct all application queries to `http://clickhouse.zengenti.io:8123` or `clickhouse.zengenti.io:9000` for native protocol.
- The `admin` user has full access, while `readonly` is ideal for analytics and reporting applications.

---

### **Best Practices**

- **Max Memory Usage:** Limited to 10GB per query (`max_memory_usage` setting).
- **Logging Level:** Set to `trace` for detailed logs (`/var/log/clickhouse-server/clickhouse-server.log`).
- **Max Connections:** 4096, with 100 concurrent queries allowed.
- **Data Compression:** The `uncompressed_cache` is disabled, optimizing for longer queries.

---

### **Access Control**

- **IP Whitelist:** Currently allows all IPs (`0.0.0.0/0`). If needed, restrict access using the `users.xml` configuration.

---

### **Monitoring & Alerting**

- **Prometheus Integration:** The cluster exposes metrics at `/metrics` on port `9363`.
- **Alerting:** Set up Prometheus alerting rules based on metrics like `max_memory_usage`, `max_connections`, and system health.

---

### **Additional Tips**

- **Backup Strategy:** If using S3, consider lifecycle rules to archive or delete old data.
- **Replication & Quorum:** Ensure ZooKeeper nodes maintain a quorum for high availability.
- **Testing:** Before deploying in production, test your integration in a staging environment to validate query performance and storage behavior.

