# Strict AWS Solutions Architect Interview: 30-Question Scenario & Trade-off Quiz

As a strict AWS Solutions Architect interviewer, I have reviewed your preparation materials. These documents cover everything from fundamental system design trade-offs to specialized AWS services and complex application architectures.

To pass this "interview," you must demonstrate not just a memorization of service names, but a deep understanding of **why** a specific architectural choice is made over another, especially regarding cost, performance, and reliability trade-offs.

---

## Part 1: Foundational Principles & Trade-offs (Chapter 1)

**1. The CAP Theorem Dilemma**
In a distributed system like the "Hotel Reservation System" (Chapter 18), you are faced with a network partition. If you prioritize **Availability** over **Consistency**, explain the specific "Soft State" risks that emerge during a peak booking period (e.g., Black Friday). How would you use AWS services to eventually reconcile the state?

**2. Synchronous vs. Asynchronous Communication**
You are designing the "Video-Processing Pipeline" (Chapter 20). Why is it technically irresponsible to use synchronous API calls between the Video Uploader and the Transcoding Engine? Which AWS messaging service would you use to decouple these, and how do you handle a "poison pill" message that keeps failing the transcoding job?

**3. The Microservices Data Dilemma (Saga Pattern)**
You are breaking down a monolithic e-commerce application into microservices (Orders, Inventory, Payments).
*   *Scenario:* A customer places an order. Inventory needs to be decremented, and Payment needs to be captured.
*   *Trade-off:* If you use synchronous REST API calls across these three services, what is the impact on availability and latency? How would you redesign this using an Event-Driven Architecture (e.g., with Amazon EventBridge or SNS/SQS), and what new challenge does this introduce regarding data consistency?

**4. Idempotency in Distributed Systems**
In the "Stock-Trading Platform" (Chapter 21), a client application sends a "Buy 100 shares of AAPL" request, but the network connection drops before it receives the acknowledgment. The client retries.
*   *Scenario:* How do you ensure the user isn't charged for 200 shares?
*   *Trade-off:* Explain how you would implement an idempotency key. What are the storage and performance trade-offs of checking this key for every single incoming transaction in a high-throughput trading system versus a lightweight API Gateway cache?

---

## Part 2: Data Storage & Persistence (Chapters 2, 3, & 10)

**5. Block vs. File vs. Object Storage**
A high-performance computing (HPC) workload requires multiple EC2 instances to have concurrent, low-latency access to a shared dataset for "Lustre" based rendering (Chapter 10). 
*   Why is **Amazon EBS** a poor choice here despite its low latency? 
*   Contrast **Amazon EFS** and **Amazon FSx for Lustre** for this specific use case.

**6. Relational vs. Non-Relational Selection**
Your "Social Network" application (Chapter 16) needs to store two types of data: 
1.  User session metadata (high frequency, simple key-value lookups).
2.  The complex "Follower/Following" graph (highly interconnected).
Explain why using **Amazon RDS (PostgreSQL)** for both might lead to a "scaling wall." Which two AWS-specific databases should you use instead, and why?

**7. Sharding Relational Databases vs. Migrating to NoSQL**
The "Online Game Leaderboard" (Chapter 17) started on Amazon RDS for MySQL. It is now hitting maximum write IOPS limits.
*   *Trade-off:* You can either shard the MySQL database or migrate to Amazon DynamoDB. Detail the operational overhead and application-level code changes required for MySQL sharding versus the data modeling paradigm shift required for DynamoDB. Which is better for a strict time-to-market constraint versus long-term maintenance?

**8. NoSQL Partitioning and the "Hot Key" Problem**
You chose Amazon DynamoDB for the "Social Network and Newsfeed System" (Chapter 16).
*   *Scenario:* A major celebrity makes a post, causing millions of users to read and comment on that specific post within seconds.
*   *Trade-off:* This creates a "hot partition" in DynamoDB, leading to throttled requests. How do you design your partition keys (e.g., using write sharding/salting) or employ caching (e.g., DAX) to mitigate this without massively over-provisioning read/write capacity for the entire table?

**9. Storage Tiering for Massive Datasets**
In the "Video-Processing Pipeline" (Chapter 20), you are storing petabytes of raw, uncompressed 4K video files in Amazon S3.
*   *Scenario:* These raw files are rarely accessed after the initial transcoding process is complete, but must be kept for 5 years for legal reasons.
*   *Trade-off:* Compare S3 Standard-IA, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. How do retrieval times and retrieval costs trade off against storage costs? At what point does compressing the archives on EC2 before sending to Glacier cost more in compute than the storage savings?

**10. Shared File Systems in the Cloud**
You need to migrate a legacy Content Management System (CMS) that requires a POSIX-compliant shared file system.
*   *Trade-off:* Compare Amazon EFS (Elastic File System) and Amazon FSx for NetApp ONTAP. If the CMS generates millions of tiny 1KB files (high metadata operations), why might EFS Standard struggle with latency, and how do Provisioned Throughput or FSx offer a trade-off between cost and IOPS performance?

---

## Part 3: Performance, Caching, & Scalability (Chapters 4 & 5)

**11. Caching Strategies & Data Freshness**
You implement a "Write-Around" caching strategy for a "Stock-Trading Platform" (Chapter 21). 
*   What is the primary risk to **Data Freshness** in this scenario? 
*   If your cache hit ratio is dropping despite plenty of memory, and you are using a **Least Recently Used (LRU)** eviction policy, what does this tell you about your access patterns?

**12. Cache Stampede (Thundering Herd) Mitigation**
Your "Hotel Reservation System" (Chapter 18) caches availability for popular destinations (e.g., "Las Vegas").
*   *Scenario:* The cache TTL expires for "Las Vegas" precisely when 5,000 concurrent users are searching for it. All 5,000 requests miss the cache and hit the underlying RDS database simultaneously, bringing it down.
*   *Trade-off:* Explain how "Cache Warming" (background refresh) versus "Mutex Locks" (only allowing one thread to query the DB while others wait) solve this. What are the latency trade-offs for the end-user in both approaches?

**13. Cache Invalidation Complexity**
In the "URL Shortener Service" (Chapter 14), you cache the mapping of short URLs to long URLs.
*   *Scenario:* A user updates the long URL destination for their custom short link.
*   *Trade-off:* Compare a "Write-Through" caching strategy versus a "Cache Invalidation" (delete from cache on write, populate on read miss) strategy. Which provides better write latency, and what is the risk of a race condition leading to stale data in the Invalidation approach?

**14. Load Balancing at Scale (L4 vs L7)**
Explain the technical difference between an **Application Load Balancer (ALB)** and a **Network Load Balancer (NLB)** in the context of the OSI model. If you are expecting a sudden burst of millions of requests per second for a "Game Leaderboard" (Chapter 17), why might an ALB fail you where an NLB would succeed without pre-warming?

**15. Internal Load Balancing for Microservices**
Inside your Kubernetes cluster (Amazon EKS) for the "Web Crawler" (Chapter 15), internal services need to communicate.
*   *Trade-off:* You can use an internal Application Load Balancer (Layer 7) or a Network Load Balancer (Layer 4) with a service mesh (like AWS App Mesh). If your primary goals are gRPC support and granular routing based on HTTP headers (e.g., A/B testing), why must you absorb the higher processing latency of L7 load balancing?

**16. Global Traffic Management**
For a global "Chat Application" (Chapter 19), users in London are experiencing high latency when connecting to a backend in North Virginia. 
*   Explain the role of **Route 53 Geoproximity Routing** vs. **Latency Routing**.
*   How does **AWS Global Accelerator** differ from using a **CloudFront CDN** for this bidirectional, stateful WebSocket traffic?

---

## Part 4: Complex System Design Case Scenarios (Chapters 14-21)

**17. Preventing "Double Booking"**
In your "Hotel Reservation System" (Chapter 18), how do you prevent two users from booking the same room simultaneously at the database level? Describe the difference between **Pessimistic Locking** (e.g., `SELECT FOR UPDATE`) and **Optimistic Locking** (using a version attribute/conditional writes in DynamoDB) and explain which is more scalable on AWS.

**18. Hotel Reservation Search Latency vs. Accuracy**
In the "Hotel Reservation System" (Chapter 18), users search for hotels by location, date, and amenities.
*   *Scenario:* You use Amazon OpenSearch (Elasticsearch) to power the complex search queries because RDS is too slow for text/geospatial searches.
*   *Trade-off:* How do you keep the OpenSearch index synchronized with the primary RDS database? If you use asynchronous replication (e.g., CDC via DynamoDB Streams or Debezium/Kafka), there is a replication lag. What is the business impact of a user seeing a room as "Available" in the search results but finding it "Sold Out" at checkout, and how do you design the UI/UX or locking mechanism to handle this graceful degradation?

**19. Base62 Encoding vs. Distributed Key Generation**
In the "URL Shortener Service" (Chapter 14), you need to generate unique 7-character short URLs.
*   *Scenario:* You can either compute a hash (MD5) of the long URL and take the first 7 characters, or you can use a distributed counter to generate an integer and convert it to Base62.
*   *Trade-off:* Hashing is stateless and fast but causes collisions. A distributed counter guarantees uniqueness but introduces a single point of failure/bottleneck. How do you mitigate the bottleneck of the distributed counter using the "Key Generation Service" (KGS) pattern, and how does KGS handle concurrency?

**20. Web Crawler BFS Frontier Management**
In the "Web Crawler and Search Engine" (Chapter 15), your URL Frontier (the queue of URLs to visit next) grows to billions of URLs.
*   *Scenario:* Keeping the frontier in RAM is no longer possible.
*   *Trade-off:* If you move the frontier to disk or a database, the crawler's throughput drops massively. How can you use a combination of in-memory queues for the active working set and disk-based storage (or SQS) for the backlog? How do you ensure politeness (not DDoSing a single domain) when pulling from a highly concurrent distributed queue?

**21. The "Fan-out" Problem in Social Networks**
In the "Social Network and Newsfeed System" (Chapter 16), user timelines are generated.
*   *Scenario:* A normal user follows 50 people. Justin Bieber follows 10 people but has 100 million followers.
*   *Trade-off:* Compare "Fan-out on Write" (Push model) versus "Fan-out on Read" (Pull model). Why does "Fan-out on Write" break down for Justin Bieber? Describe a hybrid architecture (combining push for normal users and pull for celebrities) to solve this and the engineering complexity it introduces.

**22. Leaderboard Real-time Ranking**
For the "Online Game Leaderboard" (Chapter 17), millions of players are updating their scores every minute.
*   *Scenario:* You need to display the Top 100 players globally, *and* a specific user's absolute rank (e.g., "You are rank 1,453,921").
*   *Trade-off:* A relational DB with an index can sort the top 100 quickly but `COUNT(*)` for absolute rank is incredibly slow. Using Redis Sorted Sets (`ZADD`, `ZRANK`) handles both in O(log(N)) time. What is the cost and durability trade-off of keeping the entire leaderboard in an in-memory datastore like Redis (Amazon ElastiCache) versus persisting it to an on-disk NoSQL database?

**23. Video Transcoding Chunking Strategy**
In the "Streaming Service" design (Chapter 20), we break videos into "chunks." 
*   Why do we do this instead of processing the whole file at once?
*   How do you ensure that the "Content Indexing" step only begins *after* all chunks are successfully transcoded and validated? (Hint: Think about AWS Step Functions or S3 Object tagging).

**24. Video Streaming Adaptive Bitrate (ABR)**
For the "Video-Processing Pipeline" (Chapter 20), you deliver video using HLS or DASH protocols.
*   *Scenario:* A user starts watching a movie on a 5G connection, but steps into an elevator and drops to 3G.
*   *Trade-off:* The client video player must dynamically request lower-resolution chunks. How does chunk size (e.g., 2-second chunks vs. 10-second chunks) trade-off between encoding/storage overhead and the player's ability to quickly adapt to changing network conditions without buffering?

**25. Chat App Connection Management**
The "Chat Application" (Chapter 19) maintains millions of concurrent WebSocket connections.
*   *Scenario:* The load balancer distributes connections to a fleet of EC2 instances. If an instance crashes, 100,000 users immediately drop and try to reconnect simultaneously.
*   *Trade-off:* This reconnect storm can DDoS your authentication and connection establishment services. How do you implement connection draining and exponential backoff with jitter on the client side? What is the trade-off in user experience (perceived downtime) versus backend stability?

**26. Stock Trading Event Sourcing**
In the "Online Stock-Trading Platform" (Chapter 21), every microsecond matters, and every action must be perfectly auditable.
*   *Scenario:* Instead of storing the *current state* of a user's portfolio in a traditional database table, you use Event Sourcing (storing every individual deposit, withdrawal, buy, and sell event in an immutable ledger).
*   *Trade-off:* Event Sourcing provides a perfect audit trail and allows temporal querying ("what was the portfolio state at 10:04 AM?"). However, calculating the current balance requires replaying millions of events. How do you implement "Snapshots" or CQRS (Command Query Responsibility Segregation) to mitigate the read-latency trade-off, and what consistency challenges does CQRS introduce?

---

## Part 5: AWS Compute & Operations (Chapter 11)

**27. EC2 Purchasing & Resiliency**
You have a batch processing job that is "fault-tolerant" and can be resumed if interrupted. 
*   Which EC2 pricing model (On-Demand, Reserved, or Spot) provides the best cost-to-performance ratio?
*   How do you use **Auto Scaling Groups (ASG)** to ensure that if a Spot instance is reclaimed by AWS, your job doesn't fail permanently?

**28. Serverless vs. Provisioned Compute**
The "Video-Processing Pipeline" (Chapter 20) triggers a metadata extraction script every time a new video chunk is uploaded.
*   *Scenario:* The upload rate is highly erratic—sometimes 0 per hour, sometimes 10,000 per hour.
*   *Trade-off:* Compare AWS Lambda with an Auto Scaling Group of EC2 instances. While Lambda handles the spiky scaling perfectly, what is the "Cold Start" trade-off? If the metadata extraction relies on a massive ML model library (e.g., 5GB), why might Lambda be a poor architectural choice compared to Fargate?

**29. Handling Spot Instance Interruptions at Scale**
You use EC2 Spot Instances to run the heavy transcoding jobs for the streaming service (Chapter 20).
*   *Scenario:* AWS reclaims your Spot instance with a 2-minute warning via EventBridge while it is 80% done transcoding a 2-hour movie.
*   *Trade-off:* Do you design the system to checkpoint progress every 5 minutes (increasing I/O overhead and complex state management) or do you simply restart the entire job on a new instance (wasting compute time)? Justify your choice based on cost-efficiency.

**30. Hypervisor Abstraction & Hardware Access**
In Chapter 11, the text mentions "Bare-metal servers" versus "Hypervisors" (like Xen or Nitro). 
*   *Scenario:* You are migrating an extremely latency-sensitive, proprietary in-memory database that relies heavily on direct Intel VT-x hardware instructions.
*   *Trade-off:* Why would a standard virtualized EC2 instance introduce unacceptable overhead for this workload? Explain the operational and cost trade-offs of choosing a Bare-Metal (e.g., `i3.metal`) instance over a standard EC2 instance in a high-availability architecture.
