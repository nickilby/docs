# ClickHouse Integration Guide

---

### **Overview of the ClickHouse Setup**

**Architecture:**
- The ClickHouse cluster consists of **two nodes**: `CH1`, `CH2`.
- **ZooKeeper Cluster** (for metadata sync and quorum): `ZK1`, `ZK2`, `ZK3`.
- **HAProxy** is now used as the load balancer, distributing queries to both ClickHouse nodes.
- ClickHouse nodes are set up for **internal replication** across shards.

---

### **Connecting to ClickHouse**

**Endpoints:**
- **HTTP API**: `http://clickhouse.zengenti.io:8123`
- **Native Protocol (TCP)**: `clickhouse.zengenti.io:9000`
- **MySQL Compatibility**: `clickhouse.zengenti.io:9004`
- **PostgreSQL Compatibility**: `clickhouse.zengenti.io:9005`
- **Prometheus Metrics**: `http://clickhouse.zengenti.io:9363/metrics`

**HAProxy Configuration:**
- HAProxy is configured to balance load evenly across `CH1` and `CH2`.
- Both read and write queries should be directed to the HAProxy endpoint (`clickhouse.zengenti.io`) for optimal distribution.

**Users & Authentication:**
- **Admin User:** `admin` / `poetry-gangsta-SERBIA`
- **Read-Only User:** `readonly` / `readonly`
- **Default User:** No password required.

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
- **Data Backup & Snapshots:** Use ZFS snapshots for local disks and ensure Minio/S3 is backed up if long-term storage is needed.

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

- **Prometheus Integration:** The cluster exposes metrics at `/metrics` on port `9363`. Ensure Prometheus is scraping this endpoint for performance and health metrics.
- **Alerting:** Set up Prometheus alerting rules based on metrics like `max_memory_usage`, `max_connections`, and system health.

---

### **Additional Tips**

- **Backup Strategy:** If using S3, consider lifecycle rules to archive or delete old data.
- **Replication & Quorum:** Ensure ZooKeeper nodes maintain a quorum for high availability.
- **Testing:** Before deploying in production, test your integration in a staging environment to validate query performance and storage behavior.

---

Let me know if you need specific code snippets, HAProxy configuration details, or further assistance with integrating ClickHouse into your application!

