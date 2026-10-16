# Django + Celery + Redis + RabbitMQ Interview Questions

Here are some potential interview questions covering Django, Celery, Redis, and RabbitMQ, along with explanations and edge cases:

## Django

1. **How does Django handle asynchronous tasks?**

   Django itself is primarily synchronous, but it has support for asynchronous views, middleware, and database operations as of Django 3.1+. However, Django does not provide built-in background task execution. Instead, Celery is commonly used to handle async tasks like sending emails, processing images, or performing background computations.

   - https://dev.to/pragativerma18/unlocking-performance-a-guide-to-async-support-in-django-2jdj

2. **What are Django signals, and how do they compare to Celery tasks?**

   Django signals allow decoupled components of a Django application to communicate when certain events occur. For example, the `post_save` signal can be used to trigger an action when a model instance is saved.

   **Comparison with Celery:**

   - **Signals** are synchronous and executed within the request-response cycle.
   - **Celery tasks** are asynchronous and executed in the background, preventing delays in user-facing operations.

   **Use cases:**

   - Signals: Logging, cache invalidation, simple notifications.
   - Celery: Sending emails, generating reports, and time-consuming operations.

3. **How would you scale a Django application handling high traffic?**

   To scale a Django app for high traffic:

   - **Optimize Database Queries**: Use indexing, avoid N+1 queries, leverage caching.
   - **Use Load Balancing**: Deploy multiple application servers behind a load balancer.
   - **Enable Caching**: Use Redis or Memcached for frequently accessed data.
   - **Use a CDN**: Offload static files and media files to a CDN.
   - **Use Asynchronous Task Processing**: Offload heavy tasks to Celery workers.
   - **Deploy with WSGI or ASGI**: Use Gunicorn for WSGI, or Daphne/Uvicorn for ASGI (async support).

4. **How does Django's ORM interact with databases?**

   Django ORM (Object-Relational Mapper) allows interaction with databases using Python objects instead of raw SQL. It converts Python models into SQL queries and provides an abstraction layer.

   - **QuerySet API**: `Model.objects.filter(name="John")` translates to `SELECT * FROM model WHERE name='John'`.
   - **Transactions**: Uses ACID-compliant transactions.
   - **Connection Pooling**: Managed by Django’s database engine.
   - **Lazy Execution**: QuerySets are evaluated only when necessary, improving efficiency.

5. **What happens when a database transaction fails in Django?**

   If a transaction fails:

   - If **atomic blocks** (`@transaction.atomic`) are used, Django **rolls back** all changes within the block.
   - Without atomic transactions, partial changes may persist, leading to data inconsistency.

   Example:

   ```python
   from django.db import transaction

   try:
       with transaction.atomic():
           user = User.objects.create(username="test_user")
           Profile.objects.create(user=user)  # If this fails, user creation is also rolled back
   except Exception as e:
       print("Transaction failed:", e)
   ```

6. **How does Django handle caching, and how can Redis improve performance?**

   Django supports multiple caching backends:

   - **Database caching**: Stores cache data in a database table.
   - **File system caching**: Stores cache files on disk.
   - **Memory-based caching**: Uses Memcached or Redis for high-performance caching.

   **Redis Benefits:**

   - **In-memory storage**: Faster than disk-based caching.
   - **Persistence**: Supports data persistence (RDB, AOF).
   - **Distributed Cache**: Works across multiple servers.

   Example:

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
       }
   }
   ```

7. **What happens if the Django application loses connection to the database?**

   If the database connection is lost:

   - Django raises an `OperationalError`.
   - Default behavior: Retries connections but eventually fails if the database is unreachable.
   - Solution: Use **connection pooling** and **auto-reconnect** using Django’s `CONN_MAX_AGE` setting.

   Example:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydb',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'db_host',
           'PORT': '5432',
           'CONN_MAX_AGE': 600,  # Persistent connections
       }
   }
   ```

8. **How do you secure Django applications from SQL injection, XSS, and CSRF attacks?**

   - **SQL Injection Prevention**: Django ORM escapes queries by default.
     ```python
     User.objects.get(username=username)  # Safe
     ```
   - **XSS (Cross-Site Scripting) Prevention**: Django auto-escapes templates.
     ```html
     {{ user_input }}
     <!-- Safe -->
     ```
   - **CSRF (Cross-Site Request Forgery) Prevention**: Django includes CSRF middleware.
     ```html
     <form method="post">{% csrf_token %}</form>
     ```

   Other best practices:

   - Use `SECURE_SSL_REDIRECT = True` (force HTTPS).
   - Use `HttpOnly` and `Secure` attributes on cookies.

9. **What is the difference between Django’s session storage in the database vs. in Redis?**

   Django allows session storage in:

   - **Database (`django.contrib.sessions.backends.db`)**: Stores session data in a table, leading to higher latency.
   - **Cache (Redis/Memcached)**: Stores session data in-memory, making it faster.

   **Why use Redis?**

   - **Faster retrieval** due to in-memory storage.
   - **Automatic expiration** of stale sessions.
   - **Scalability** for distributed applications.

10. **How do you manage background tasks in Django without Celery?**

    While Celery is the preferred choice for background tasks, alternatives include:

    1. **Django-cron**:
       - Runs periodic tasks based on system cron jobs.
       - Example:
         ```python
         from django_cron import CronJobBase, Schedule
         class MyCronJob(CronJobBase):
             RUN_EVERY_MINS = 60  # every hour
             schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
             code = 'my_app.my_cron_job'
             def do(self):
                 print("Running background task")
         ```
    2. **Threading in Django Views** (not recommended for heavy tasks):

       ```python
       import threading
       def process_data():
           # Expensive operation
           pass

       t = threading.Thread(target=process_data)
       t.start()
       ```

    3. **Using Django’s `runserver` with Management Commands**:
       - Custom command:
         ```python
         from django.core.management.base import BaseCommand
         class Command(BaseCommand):
             def handle(self, *args, **kwargs):
                 print("Executing background task")
         ```
       - Run as:
         ```bash
         python manage.py my_custom_command
         ```
    4. **Database-backed queue**:
       - Use Django’s ORM to store tasks and process them with a simple worker script.

    While these alternatives work, Celery provides better reliability, scheduling, and retry mechanisms.

## Celery

1. **What is Celery, and why is it used?**

   Celery is an asynchronous task queue based on distributed message passing. It is used to offload long-running or background tasks from the main application, improving responsiveness and performance.

   **Common Use Cases:**

   - Sending emails asynchronously.
   - Processing large datasets.
   - Scheduling periodic tasks (e.g., reports, data backups).
   - Handling web scraping jobs.

2. **How does Celery execute tasks asynchronously?**

   Celery follows a producer-consumer architecture where:

   1. A **producer (Django app)** sends a task to a **message broker** (Redis/RabbitMQ).
   2. A **Celery worker** picks up the task from the broker and processes it.
   3. The result is optionally stored in a **results backend** (Redis, database, etc.).

   ![image.png](Django%20+%20Celery%20+%20Redis%20+%20RabbitMQ%20Interview%20Quest%201a0ac7d04d878032b379c840b387c722/image.png)

3. **What are the different Celery message brokers, and how do they compare?**

   Celery supports multiple message brokers:

   - **Redis** (fast in-memory store, supports pub/sub, but may lose tasks if not persistent).
   - **RabbitMQ** (persistent queues, better message durability).
   - **Amazon SQS** (fully managed, highly available, but higher latency).

   **Comparison:**

   | Feature     | Redis                  | RabbitMQ             | Amazon SQS        |
   | ----------- | ---------------------- | -------------------- | ----------------- |
   | Speed       | Faster (in-memory)     | Slower (disk-based)  | Slower            |
   | Persistence | Optional (RDB/AOF)     | Yes (durable queues) | Yes               |
   | Scalability | Horizontal scaling     | Clustering required  | Auto-scaled       |
   | Use Case    | Quick, transient tasks | Reliable messaging   | Cloud-native apps |

4. **What happens if a Celery task fails?**

   By default, failed tasks are logged, but they can be retried using `retry`.

   Example:

   ```python
   from celery import shared_task
   from celery.exceptions import MaxRetriesExceededError
   import requests

   @shared_task(bind=True, max_retries=3)
   def fetch_url(self, url):
       try:
           response = requests.get(url)
           return response.text
       except requests.RequestException as exc:
           raise self.retry(exc=exc, countdown=5)  # Retries after 5 seconds
   ```

   - The task retries up to **3 times** before failing permanently.
   - `countdown=5` adds a delay before retries.

5. **What happens if the Celery worker crashes?**

   - Any task in progress **may be lost** if it was running in memory.
   - If using **RabbitMQ** (durable queues), unprocessed tasks remain in the queue.
   - If using **Redis**, tasks might be lost unless `acks_late=True` is used.
   - Celery can recover tasks with **task acknowledgment** enabled.

   Solution: Enable **task persistence** using:

   ```python
   task_acks_late = True  # Ensures tasks are acknowledged after execution
   worker_prefetch_multiplier = 1  # Ensures fair task distribution
   ```

   ### Is the Task Lost If a Worker Crashes?

   | **When Worker Crashes?**                | **Is Task Lost?** | **Solution**                                   |
   | --------------------------------------- | ----------------- | ---------------------------------------------- |
   | **Before fetching task**                | ❌ No             | Task is still in queue                         |
   | **After fetching but before execution** | ✅ Yes (default)  | `acks_late=True`                               |
   | **During execution**                    | ✅ Yes (default)  | `acks_late=True`, `autoretry_for=(Exception,)` |
   | **After execution (completed task)**    | ❌ No             | Task is done                                   |

6. **How does Celery handle scheduled and periodic tasks?**

   Celery can schedule tasks using **Celery Beat**, a periodic task scheduler.

   Example:

   ```python
   from celery.schedules import crontab
   from celery import Celery

   app = Celery('tasks')

   app.conf.beat_schedule = {
       'every-day-task': {
           'task': 'tasks.daily_report',
           'schedule': crontab(hour=0, minute=0),
       },
   }
   ```

   This runs `daily_report` every day at midnight.

7. **What happens if Redis (or RabbitMQ) crashes while a task is in progress?**

   - **Redis as broker**: Tasks might be lost unless they are persistent.
   - **RabbitMQ as broker**: Messages remain in the queue due to durability settings.
   - **Result backend impact**: If Redis is the result backend, results might be lost.

   Solution:

   - Use **persistent queues** in RabbitMQ (`x-ha-policy: all` for HA queues).
   - Enable **AOF persistence** in Redis to reduce data loss.
   - Configure **retry policies** in Celery tasks.

8. **How do you handle task dependencies in Celery?**

   Celery provides **chaining**, **groups**, and **callbacks** for task dependencies.

   **Task Chain (Sequential Execution)**:

   ```python
   from celery import chain

   chain(task1.s(), task2.s(), task3.s())()
   ```

   **Task Group (Parallel Execution)**:

   ```python
   from celery import group

   group(task1.s(), task2.s(), task3.s())()
   ```

   **Chord (Parallel + Callback)**:

   ```python
   from celery import chord

   chord([task1.s(), task2.s()])(callback_task.s())
   ```

9. **What are Celery's different states (PENDING, STARTED, SUCCESS, FAILURE, etc.)?**

   Celery tasks have different states:

   - **PENDING**: Task is in the queue but not yet assigned.
   - **STARTED**: Task execution has begun (requires `task_track_started=True`).
   - **RETRY**: Task has failed but is retrying.
   - **SUCCESS**: Task executed successfully.
   - **FAILURE**: Task execution failed.

10. **What is the differences Between Celery Workers, Task Queues, Message Brokers, and Result Backends?**

    | **Component**       | **Definition**                          | **Purpose**                                                   | **Examples**                               |
    | ------------------- | --------------------------------------- | ------------------------------------------------------------- | ------------------------------------------ |
    | **Celery Workers**  | Processes that execute Celery tasks.    | Consume tasks from queues and execute them asynchronously.    | `celery worker -A myapp`                   |
    | **Task Queues**     | Queues that hold pending tasks.         | Stores tasks until they are picked up by a worker.            | `default`, `high-priority`, `low-priority` |
    | **Message Brokers** | Middleware that routes tasks to queues. | Transfers tasks from the producer (Django app) to the worker. | Redis, RabbitMQ, Amazon SQS                |
    | **Result Backends** | Stores task execution results.          | Allows retrieval of task status and results.                  | Redis, PostgreSQL, MongoDB, Memcached      |

    ***

    ### **Detailed Breakdown**

    ### **1. Celery Workers**

    - Workers are background processes that execute tasks asynchronously.
    - They listen for tasks in a queue and process them when available.
    - Multiple workers can run on different machines to scale task execution.

    **Example: Starting a worker**

    ```bash
    celery -A myapp worker --loglevel=info
    ```

    - `A myapp`: Specifies the Celery app.
    - `worker`: Starts a worker process.
    - `-loglevel=info`: Sets log verbosity.

    ***

    ### **2. Task Queues**

    - Task queues hold tasks that are waiting to be processed.
    - Workers consume tasks from these queues in a FIFO manner.
    - Tasks can be routed to different queues based on priority.

    **Example: Defining a queue in Celery**

    ```python
    from celery import Celery

    app = Celery('myapp', broker='redis://localhost:6379/0')

    app.conf.task_routes = {
        'tasks.high_priority': {'queue': 'high_priority'},
        'tasks.low_priority': {'queue': 'low_priority'},
    }
    ```

    - Tasks are routed based on the function name.

    **Sending a task to a specific queue**

    ```python
    add.apply_async(args=[4, 4], queue='high_priority')
    ```

    ***

    ### **3. Message Brokers**

    - A message broker acts as an intermediary between producers (Django app) and consumers (workers).
    - It ensures tasks are stored in queues until workers are ready to process them.

    **Popular Message Brokers:**

    | Broker         | Pros                                                     | Cons                                          |
    | -------------- | -------------------------------------------------------- | --------------------------------------------- |
    | **Redis**      | Fast, simple setup, supports Pub/Sub.                    | Volatile memory storage, potential data loss. |
    | **RabbitMQ**   | Persistent queues, message durability, advanced routing. | More complex setup.                           |
    | **Amazon SQS** | Fully managed, scalable.                                 | Higher latency, additional cost.              |

    ***

    ### **4. Result Backends**

    - The result backend stores task statuses and return values.
    - If a task returns a result, it can be retrieved later.
    - Some backends support expiration policies to delete old results.

    **Example: Storing results in Redis**

    ```python
    app.conf.result_backend = 'redis://localhost:6379/0'
    ```

    **Checking task status**

    ```python
    result = add.delay(4, 4)
    print(result.status)  # PENDING, SUCCESS, FAILURE
    print(result.get())   # Fetch result
    ```

    **Common result backends:**

    | Backend    | Pros                             | Cons                         |
    | ---------- | -------------------------------- | ---------------------------- |
    | Redis      | Fast, in-memory storage.         | Data loss if not persistent. |
    | PostgreSQL | Durable, SQL queries supported.  | Slower than Redis.           |
    | MongoDB    | Flexible, supports complex data. | Additional setup required.   |

11. **Why Do We Need Message Brokers If Queues Already Exist?**

    At first glance, it might seem like **task queues** should be enough to handle background tasks. However, **message brokers** provide essential functionality that simple queues alone cannot offer. Here’s why message brokers are necessary:

    ### **1. Message Brokers Manage Queues Efficiently**

    A **queue** is just a storage structure for tasks, but it does not have the intelligence to:

    - Route messages to the right workers.
    - Ensure message delivery reliability.
    - Handle multiple producers and consumers efficiently.

    A **message broker** (like Redis or RabbitMQ) **manages** queues by:

    - Storing tasks in memory or disk.
    - Ensuring tasks are delivered to the right queue.
    - Handling retries, acknowledgments, and routing.

    Without a broker, we would need to manually implement all of these features.

    ### **2. Message Brokers Ensure Reliability & Durability**

    - If a queue were just a simple data structure (e.g., a Python list or database table), **tasks could be lost** if the system crashes.
    - Brokers like **RabbitMQ** provide **persistent queues**, ensuring that tasks survive restarts.
    - **Redis** allows for **data persistence** using **Append-Only File (AOF) mode**.

    📌 **Example:**

    If a worker crashes while processing a task, RabbitMQ **re-delivers** the task to another worker.

    ***

    ### **3. Message Brokers Allow Asynchronous Communication**

    - The **producer (Django app)** doesn’t have to wait for the task to complete—it just **sends** it to the broker and moves on.
    - The **worker** picks up the task when it’s available, processes it, and sends the result back.
    - This enables **scalability** and **non-blocking execution**.

    📌 **Example:**

    A Django app sending 1,000 emails should **not** process them synchronously—it should push them to a broker like Redis, and multiple Celery workers can process them in parallel.

    ***

    ### **4. Message Brokers Support Multiple Consumers & Load Balancing**

    - A single queue can be **shared among multiple workers**, distributing tasks efficiently.
    - Brokers like RabbitMQ **load-balance** tasks among multiple workers using **round-robin scheduling**.

    📌 **Example:**

    If 5 workers are listening to a queue, the broker distributes tasks among them dynamically.

    ***

    ### **5. Message Brokers Support Advanced Task Routing**

    - Some tasks may be **high-priority**, while others can wait.
    - Brokers **route tasks to different queues** based on predefined rules.

    📌 **Example:**

    A web scraping job may go to a **low-priority queue**, while a payment processing job goes to a **high-priority queue**.

    ```python
    app.conf.task_routes = {
        'tasks.process_payment': {'queue': 'high_priority'},
        'tasks.web_scrape': {'queue': 'low_priority'},
    }
    ```

    ***

    ### **6. Message Brokers Handle Retries & Acknowledgments**

    - If a worker crashes while processing a task, a broker ensures the task is **retried**.
    - Celery allows enabling **acknowledgments**, meaning the broker considers a task **complete only when the worker confirms it**.

    📌 **Example:**

    If `task_acks_late=True` is enabled in Celery, a task will only be removed from the queue **after** successful execution.

    ```python
    app.conf.task_acks_late = True
    ```

    ***

    ### **7. Message Brokers Scale With the System**

    - As the number of tasks grows, brokers handle **thousands to millions of tasks** efficiently.
    - They support **distributed task execution**, meaning multiple workers across different servers can process tasks from a single broker.

    📌 **Example:**

    In a cloud-based architecture, **multiple workers on different servers** can pull tasks from a **single broker instance**.

    ***

    ### **Summary: Why Not Just Use Queues?**

    | Feature                            | Simple Queue (e.g., Python List, DB Table) | Message Broker (Redis, RabbitMQ)                 |
    | ---------------------------------- | ------------------------------------------ | ------------------------------------------------ |
    | **Persistence**                    | No (tasks lost on crash)                   | Yes (Redis AOF, RabbitMQ durable queues)         |
    | **Asynchronous Execution**         | No (blocking execution)                    | Yes (non-blocking)                               |
    | **Load Balancing**                 | No (one queue = one consumer)              | Yes (multiple workers consume tasks dynamically) |
    | **Task Retries & Acknowledgments** | No (manual handling)                       | Yes (automatic retries, acks)                    |
    | **Task Routing & Prioritization**  | No                                         | Yes (priority queues, routing rules)             |
    | **Scalability**                    | Low (single queue = single system)         | High (distributed processing)                    |

12. **Where Do Queues Exist in Celery?**

    The queues in Celery are **not stored inside Celery itself**—they exist **within the message broker** (like Redis or RabbitMQ). Celery **only interacts with these queues** to send and receive tasks.

    ### **How Celery Queues Work?**

    1. **Django (or any producer) sends a task** → The task is pushed into a queue inside the message broker.
    2. **The broker holds the queue** until a worker picks up the task.
    3. **Celery workers consume tasks** from these queues and execute them.

    ### **Where Do These Queues Physically Exist?**

    It depends on the message broker being used:

    | **Message Broker** | **Where Queues Exist?**                                                                                                   |
    | ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
    | **Redis**          | Queues exist as **lists** inside Redis memory (e.g., `LPUSH` for adding tasks, `RPOP` for consuming).                     |
    | **RabbitMQ**       | Queues exist as **durable message queues** inside RabbitMQ (AMQP-based). Messages are stored temporarily until processed. |
    | **Amazon SQS**     | Queues exist inside Amazon’s managed Simple Queue Service (SQS), persisting messages until consumed.                      |
    | **Kafka**          | Queues exist as **partitions inside Kafka topics**, allowing scalable message streaming.                                  |

## Redis

1. **How does Redis differ from traditional databases?**

   | Feature              | Redis                                        | Traditional Databases (PostgreSQL, MySQL, etc.) |
   | -------------------- | -------------------------------------------- | ----------------------------------------------- |
   | **Storage**          | In-memory                                    | Disk-based                                      |
   | **Speed**            | Extremely fast                               | Slower (disk I/O involved)                      |
   | **Data Persistence** | Optional (AOF, RDB)                          | Persistent by default                           |
   | **Data Model**       | Key-value                                    | Relational (tables, joins)                      |
   | **Transactions**     | Supports transactions, but limited           | Full ACID compliance                            |
   | **Scalability**      | Scales horizontally (sharding, clustering)   | Can be scaled but needs optimizations           |
   | **Use Cases**        | Caching, message queues, real-time analytics | OLTP, relational data storage                   |

   Redis is **not a replacement** for traditional databases but is used for caching, real-time operations, and message brokering.

2. **What happens if Redis crashes while it is storing Celery task states?**

   - If Redis is being used as a **Celery result backend**, all task states **will be lost** unless persistence is enabled.
   - Tasks that are **queued but not yet fetched** may also be lost.
   - Running tasks **continue** if they have already been picked up by workers.

   ✅ **Solution:**

   - Enable Redis **AOF (Append-Only File) or RDB snapshots** for persistence.
   - Use an **alternative result backend** (e.g., PostgreSQL, S3, or RabbitMQ) to avoid losing task states.

3. **How can Redis persistence be enabled, and what are the trade-offs?**

   Redis provides **two persistence mechanisms**:

   1. **RDB (Redis Database Backup) – Periodic Snapshots**

      - Saves a snapshot of the dataset **at intervals** (e.g., every 5 minutes).
      - Less disk I/O but **risk of data loss** between snapshots.
      - ✅ **Good for caching, not for critical data.**
      - 🔴 **Trade-off:** Data loss possible if Redis crashes between snapshots.

      **Enable RDB:**

      ```
      save 900 1   # Save every 900 seconds if at least 1 change
      save 300 10  # Save every 300 seconds if at least 10 changes
      ```

   2. **AOF (Append-Only File) – Continuous Logging**

      - Logs every write operation **to disk** for full recovery.
      - ✅ **Best for Celery queues and critical tasks.**
      - 🔴 **Trade-off:** More disk usage and I/O overhead.

      **Enable AOF:**

      ```
      appendonly yes
      appendfsync everysec  # Sync to disk every second
      ```

   ✅ **Best Practice:** Use **both AOF and RDB** for better recovery.

4. **What happens if Redis runs out of memory?**

   - Redis **stops accepting writes** once it reaches the `maxmemory` limit.
   - If `maxmemory-policy` is set, it starts **evicting old keys** (depending on policy).
   - If no eviction policy is set, Redis **throws errors** for new writes.

   ✅ **Solutions:**

   - Increase `maxmemory`:
     ```
     maxmemory 2gb
     ```
   - Set an eviction policy (`allkeys-lru`, `volatile-lru`, etc.):
     ```
     maxmemory-policy allkeys-lru
     ```

5. **How does Redis handle concurrency?**

   - Redis is **single-threaded** but **uses an event loop** to handle multiple requests.
   - It executes commands **one at a time** in sequence (Atomic operations).
   - **Pipelining** allows sending multiple commands at once, improving performance.
   - **Transactions (`MULTI/EXEC`)** ensure multiple operations are executed atomically.

   ✅ **Best Practices:**

   - Use **pipelining** for batch operations.
   - Use **Lua scripts** for atomic multi-step operations.
   - Scale Redis with **sharding and clustering**.

6. **What are Redis pub/sub and its use cases?**
   - **Publish/Subscribe (Pub/Sub)** allows message broadcasting.
   - **Publishers** send messages to channels, and **subscribers** receive them.
   - **Use Cases:**
     - **Real-time notifications** (e.g., chat apps, live updates).
     - **Event-driven architecture** (decoupling microservices).
     - **Streaming data processing** (e.g., logs, monitoring).
7. **How does Redis replication work, and how do you handle failover?**
   - Redis **replicates** data from a **primary (master) node** to **one or more replicas (slaves)**.
   - Replicas sync **asynchronously**.
   - Failover is handled using **Redis Sentinel** or **Redis Cluster**.
8. **What are the differences between Redis and RabbitMQ as message brokers?**

   | Feature           | Redis                           | RabbitMQ                                   |
   | ----------------- | ------------------------------- | ------------------------------------------ |
   | **Message Model** | Pub/Sub & Streams               | AMQP Queues                                |
   | **Persistence**   | Optional (AOF/RDB)              | Persistent by default                      |
   | **Reliability**   | Less reliable (default)         | Highly reliable                            |
   | **Ordering**      | FIFO not guaranteed             | FIFO & priority queues available           |
   | **Scalability**   | Horizontally scalable           | Needs clustering for scale                 |
   | **Best For**      | Fast, real-time data processing | Reliable task queues, event-driven systems |

   ✅ **When to Use Redis?**

   - Low-latency tasks (real-time updates, analytics).
   - Lightweight pub/sub messaging.

   ✅ **When to Use RabbitMQ?**

   - Reliable, **persistent** message queues.
   - Ensuring **no task loss** in Celery.

9. **What happens if Redis gets overloaded with too many Celery tasks?**

   - High CPU and memory usage.
   - Redis may **reject new tasks** if `maxmemory` is reached.
   - Celery workers may **timeout waiting for tasks**.

   ✅ **Solutions:**

   1. **Increase Redis memory limit** or **enable eviction policy**.
   2. **Use multiple Redis instances (sharding).**
   3. **Switch to RabbitMQ** for a more **scalable** message broker.
   4. **Use Celery rate limiting** to prevent task floods

10. **How do you secure Redis from unauthorized access and attacks?**

    1. **Bind Redis to localhost (prevent external access)**

       ```
       bind 127.0.0.1
       ```

    2. **Set a strong Redis password (`requirepass`)**

       ```
       requirepass MySecurePass
       ```

    3. **Disable dangerous commands (flushall, config, shutdown)**

       ```
       rename-command FLUSHALL ""
       rename-command CONFIG ""
       ```

    4. **Enable TLS Encryption**

       ```
       tls-cert-file /etc/ssl/redis.crt
       tls-key-file /etc/ssl/redis.key
       ```

    5. **Use a firewall (`ufw` or `iptables`)** to restrict access.

       ```
       sudo ufw allow from 192.168.1.100 to any port 6379
       ```

    ✅ **Best Practice:** Deploy Redis **behind a VPN** or **inside a private network**.

## RabbitMQ

1. **How does RabbitMQ work as a message broker for Celery?**

   RabbitMQ is a **reliable** message broker that Celery uses to queue tasks and ensure delivery. It supports **durable queues, message acknowledgments, and retries**, making it a better choice for **persistent and fault-tolerant** task queues.

   1. **Producer (Django/Celery Task) publishes a task** → Sent to an **Exchange**
   2. **Exchange routes the task** → Pushed into a **Queue** (based on bindings)
   3. **Consumer (Celery Worker) fetches the task** → Acknowledges completion after processing

   ✅ **Why RabbitMQ?**

   - Supports **persistent queues** (tasks survive restarts).
   - Ensures **only one worker picks a task** (FIFO processing).
   - Built-in **acknowledgment & retry mechanisms** prevent task loss.

2. **What is the difference between Redis and RabbitMQ as Celery brokers?**

   | Feature         | Redis                          | RabbitMQ                      |
   | --------------- | ------------------------------ | ----------------------------- |
   | **Data Model**  | Key-Value Store                | AMQP-based Message Queue      |
   | **Persistence** | Optional (AOF, RDB)            | Persistent by default         |
   | **Ordering**    | FIFO not guaranteed            | FIFO guaranteed               |
   | **Reliability** | Less reliable (may drop tasks) | Highly reliable               |
   | **Scalability** | Sharding, clustering           | Clustering, high availability |
   | **Use Case**    | Fast, real-time jobs           | Guaranteed delivery of tasks  |

   **When to use Redis?**

   - **High-speed** tasks (caching, low-priority jobs).
   - If **task loss is acceptable**.

   **When to use RabbitMQ?**

   - If **task persistence is required**.
   - **Ensuring at-least-once task execution**.

3. **How does RabbitMQ handle message acknowledgments and retries?**

   - When a worker **fetches a task**, RabbitMQ marks it as **unacknowledged**.
   - The task is **removed from the queue only after acknowledgment** (`ack`).
   - If the worker **crashes before ack**, RabbitMQ **requeues** the task automatically.
   - RabbitMQ supports **automatic retries** if a task fails.

   ✅ **Explicit Acknowledgment in Celery:**

   ```python
   @app.task(acks_late=True)  # Ensures message is acknowledged only after completion
   def process_task():
       ...
   ```

4. **What happens if RabbitMQ crashes while tasks are in the queue?**

   - If queues are **non-durable**, all tasks are **lost**.
   - If queues are **durable** and messages are **persistent**, tasks survive a crash.

   ✅ **Solution:**

   - **Enable durable queues**:
     ```python
     app.conf.task_queues = Queue('default', durable=True)
     ```
   - **Use persistent messages**:
     ```python
     app.conf.task_serializer = 'json'
     app.conf.result_persistent = True
     ```

5. **What is the purpose of RabbitMQ’s exchange, queue, and binding?**

   RabbitMQ routes messages using an **Exchange**, which determines how tasks reach queues.

   - **Exchange**: Routes messages based on rules (`direct`, `fanout`, `topic`).
   - **Queue**: Stores messages until a worker consumes them.
   - **Binding**: Connects exchanges to queues based on rules.

   ✅ **Example:**

   ```python
   # Direct exchange
   app.conf.task_queues = (
       Queue('tasks', Exchange('default'), routing_key='task_queue'),
   )
   ```

6. **How can RabbitMQ ensure message durability?**
   - **Declare durable queues:**
     ```python
     Queue('default', durable=True)
     ```
   - **Enable persistent messages:**
     ```python
     app.conf.task_serializer = 'json'
     app.conf.result_persistent = True
     ```
   - **Use mirrored queues (HA Mode)** in clustered RabbitMQ.
7. **What happens if a consumer crashes after consuming a message?**

   - If the worker **did not acknowledge** the message, RabbitMQ **requeues it**.
   - If **acknowledgment was sent**, the message is **lost** unless a result backend is used.

   ✅ **Solution:** Use `acks_late=True` to avoid losing tasks.

   ```python
   @app.task(acks_late=True)
   def process_task():
       ...
   ```

8. **How do you scale RabbitMQ for high availability?**
   - **Use Clustering** – Deploy multiple RabbitMQ nodes.
   - **Enable High-Availability Queues** – Mirror queues across nodes:
     ```
     rabbitmqctl set_policy ha-all ".*" '{"ha-mode":"all"}'
     ```
   - **Load balancing** – Use **HAProxy** or **NGINX**.
9. **What happens if RabbitMQ queues get overloaded?**
   - If RabbitMQ gets overloaded, it **rejects new tasks** or **slows down consumers**.
   - **Enable flow control** to prevent overload:
     ```
     rabbitmqctl set_vm_memory_high_watermark 0.6
     ```
   - **Increase prefetch limit** to improve throughput:
     ```python
     app.conf.worker_prefetch_multiplier = 10
     ```
10. **How does RabbitMQ handle delayed message delivery?**

    RabbitMQ does not natively support delayed messages but can use **Dead Letter Exchanges (DLX)**.

    ✅ **Example: Delay Message Processing by 10s**

    ```python
    app.conf.task_routes = {'tasks.slow_task': {'queue': 'delayed'}}
    ```

---


# DRF Interview Questions & Answers

---

### Table of Contents
| No. | Questions |
| --- | --------- |
|   | **[Core Concepts](#core-concepts)** |
|1  | [What is an API?](#what-is-an-api) |
|2  | [What is a web API?](#what-is-a-web-api) |
|3  | [What is a REST API?](#what-is-a-rest-api) |
|4  | [What is an endpoint?](#what-is-an-endpoint) |
|5  | [What are HTTP Verbs?](#what-are-http-verbs) |
|6  | [What is the difference between HTTP and HTTPS?](#what-is-the-difference-between-http-and-https) |
|7  | [What are status codes?](#what-are-status-codes) |
|8  | [What is the difference between authentication and authorization?](#what-is-the-difference-between-authentication-and-authorization) |
|9  | [What is a browsable API?](#what-is-a-browsable-api)|
|10  | [What is CORS?](#what-is-cors) |
|11  | [How to fix CORS error in Django?](#how-to-fix-cors-error-in-django) |
|12 | [What is the difference between stateful and stateless?](#what-is-the-difference-between-stateful-and-stateless)  |
|  | **[Django Rest Framework](#django-rest-framework)**  |
|1  | [What is Django Rest Framework?](#what-is-django-rest-framework) |
|2  | [What are benefits of using Django Rest Framework?](#what-are-benefits-of-using-django-rest-framework) |
|3  | [What are serializers?](#what-are-serializers) |
|4  | [What are Permissions in DRF?](#what-are-permissions-in-drf) |
|5  | [How to add login in the browsable API provided by DRF?](#how-to-add-login-in-the-browsable-api-provided-by-drf) |
|6  | [What are Project-Level Permissions?](#what-are-project-level-permissions) |
|7  | [How to make custom permission classes?](#how-to-make-custom-permission-classes)|
|8  | [What is Basic Authentication?](#what-is-basic-authentication) |
|9  | [What are the disadvantages of Basic Authentication?](#what-are-the-disadvantages-of-basic-authentication) |
|10  | [What is session authentication?](#what-is-session-authentication) |
|11  | [What are the pros and cons of session authentication?](#what-are-the-pros-and-cons-of-session-authentication) |
|12  | [What is Token Authentication?](#what-is-token-authentication) |
|13  | [What are pros and cons of token authentication?](#what-are-pros-and-cons-of-token-authentication) |
|14  | [What is the difference between cookies vs localStorage?](#what-is-the-difference-between-cookies-vs-localstorage) |
|15  | [Where should token be saved - cookie or localStorage?](#where-should-token-be-saved-cookie-or-localstorage) |
|16  | [What are disadvantages of Django REST Framework's built-in TokenAuthentication?](#what-are-disadvantages-of-django-rest-framework-s-built-in-tokenauthentication) |
|17  | [What are JSON Web Tokens(JWTs)?](#what-are-json-web-tokens-jwts)  |
|18  | [What are benefits of JWT?](#what-are-benefits-of-jwt) |
|19  | [What is the difference between a session and cookie?](#what-is-the-difference-between-a-session-and-cookie) |
|20  | [What is the difference between cookie and tokens?](#what-is-the-difference-between-cookie-and-tokens) |
|21  | [What's an access token?](#what-s-an-access-token) |
|22  | [What is meant by a bearer token?](#what-is-meant-by-a-bearer-token) |
|23  | [What is the security threat to access token?](#what-is-the-security-threat-to-access-token) |
|24  | [What is a refresh token?](#what-is-a-refresh-token) |
|25  | [What are the best practices when using token authentication?](#what-are-the-best-practices-when-using-token-authentication) |
|26  | [What is cookie-based authentication?](#what-is-cookie-based-authentication) |
|27  | [What are viewsets in DRF?](#what-are-viewsets-in-drf) |
|28  | [What are routers in DRF?](#what-are-routers-in-drf) |
|29  | [What is the difference between APIViews and Viewsets in DRF?](#what-is-the-difference-between-apiviews-and-viewsets-in-drf) |
|30  | [What is the difference between `GenericAPIView` and `GenericViewset`?](#what-is-the-difference-between-genericapiview-and-genericviewset) |
| | [About Author](#about-author) | 
| | [Connect with me](#connect-with-me)| 


---

## Core Concepts


    
1. ### What is an API?
   An API is a set of definitions and protocols for building and integrating application software. API stands for **Application Programming Interface**. APIs let your product or service communicate with other products and services without having to know how they’re implemented. This can simplify app development, saving time and money. The API is not the database or even the server; it’s the code that governs the access point(s) for the server. 

   It’s sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer (the call) and the content required by the producer (the response). For example, the API design for a weather service could specify that the user supply a zip code and that the producer reply with a 2-part answer, the first being the high temperature, and the second being the low. 


   **[⬆ Back to Top](#table-of-contents)**

2. ### What is a web API?
   A web API is a collection of endpoints that expose certain parts of an underlying database. As developers we control the URLs for each endpoint, what underlying data is available, and what actions are possible via HTTP verbs.


   **[⬆ Back to Top](#table-of-contents)**

3. ### What is a REST API?
   A **REST(Representational State Transfer) API** (also known as RESTful API) is an API that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services. When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. 

   Every RESTful API:

   - is stateless, like HTTP
   - supports common HTTP verbs (GET, POST, PUT, DELETE, etc.)
   - returns data in either the JSON or XML format

   Any RESTful API must, at a minimum, have these three principles. The standard is important because it provides a consistent way to both design and consume web APIs.

   **[⬆ Back to Top](#table-of-contents)**

4. ### What is an endpoint?
   A web API has endpoints - URLs with a list of available actions (HTTP verbs) that expose data (typically in JSON, which is the most common data format these days and the default for Django REST Framework).

   The type of endpoint which returns multiple data resources is known as a **collection.**

   **[⬆ Back to Top](#table-of-contents)**

5. ### What are HTTP Verbs?
   HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. Although they can also be nouns, these request methods    are sometimes referred to as HTTP verbs.
   ![HTTP Verbs](https://user-images.githubusercontent.com/42115530/104155356-08919a00-540d-11eb-94f8-316e8f591177.png)

   **[⬆ Back to Top](#table-of-contents)**

6. ### What is the difference between HTTP and HTTPS?
   HTTPS stands for Hypertext Transfer Protocol Secure (also referred to as HTTP over TLS or HTTP over SSL). HTTPS also uses TCP (Transmission Control Protocol) to send and receive data packets, but it does so over port 443, within a connection encrypted by Transport Layer Security (TLS). Generally sites running over HTTPS will have a redirect in place so even if you type in `http://` it will redirect to deliver over a secured connection.

   **Key Differences:**

  - HTTP is unsecured while HTTPS is secured.
  - HTTP sends data over port 80 while HTTPS uses port 443.
  - HTTP operates at application layer, while HTTPS operates at transport layer.
  - No SSL certificates are required for HTTP, with HTTPS it is required that you have an SSL certificate and it is signed by a CA.
  - HTTP doesn't require domain validation, where as HTTPS requires at least domain validation and certain certificates even require legal document validation.
  - No encryption in HTTP, with HTTPS the data is encrypted before sending.

   **[⬆ Back to Top](#table-of-contents)**

7. ### What are status codes?
   HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
  - **1xx: Informational** – Communicates transfer protocol-level information.
  - **2xx: Success** – Indicates that the client’s request was accepted successfully.
  - **3xx: Redirection** – Indicates that the client must take some additional action in order to complete their request.
  - **4xx: Client Error** – This category of error status codes points the finger at clients.
  - **5xx: Server Error** – The server takes responsibility for these error status codes.

   **[⬆ Back to Top](#table-of-contents)**
   
8. ### What is the difference between authentication and authorization?
   Authentication confirms that users are who they say they are. Authorization gives those users permission to access a resource. In secure environments, authorization must always follow authentication. Users should first prove that their identities are genuine before an organization’s administrators grant them access to the requested resources.
   
   Let's use an analogy to outline the differences.

   Consider a person walking up to a locked door to provide care to a pet while the family is away on vacation. That person needs:

   Authentication, in the form of a key. The lock on the door only grants access to someone with the correct key in much the same way that a system only grants access to users who have the correct credentials.
   Authorization, in the form of permissions. Once inside, the person has the authorization to access the kitchen and open the cupboard that holds the pet food. The person may not have permission to go into the bedroom for a quick nap. 
   
   **[⬆ Back to Top](#table-of-contents)**
   
9. ### What is a browsable API?
   Django REST Framework supports generating human-friendly HTML output for each resource when the HTML format is requested. These pages allow for easy browsing of resources, as well as forms for submitting data to the resources using POST, PUT, and DELETE. It facilitates interaction with RESTful web service through any web browser. To enable this feature, we should specify text/html for the Content-Type key in the request header.

   **[⬆ Back to Top](#table-of-contents)**

10. ### What is CORS?
    Cross-Origin Resource Sharing (CORS) is a protocol that enables scripts running on a browser client to interact with resources from a different origin. This is useful because, thanks to the same-origin policy followed by XMLHttpRequest and fetch, JavaScript can only make calls to URLs that live on the same origin as the location where the script is running.

    **[⬆ Back to Top](#table-of-contents)**
   
11. ### How to fix CORS error in Django?
    CORS requires the server to include specific HTTP headers that allow for the client to determine if and when cross-domain requests should be allowed.

    The easiest way to handle this–-and the one recommended by Django REST Framework–-is to use middleware that will automatically include the appropriate HTTP headers based on our settings.

    We use `django-cors-headers`:

    - add `corsheaders` to the `INSTALLED_APPS`
    - add `CorsMiddleware` above `CommonMiddleWare` in `MIDDLEWARE`
    - create a `CORS_ORIGIN_WHITELIST` 
   
   
    **[⬆ Back to Top](#table-of-contents)**

12. ### What is the difference between stateful and stateless?
    A stateless process or application can be understood in isolation. There is no stored knowledge of or reference to past transactions. Each transaction is made as if from scratch for the first time.

    Stateful applications and processes, however, are those that can be returned to again and again, like online banking or email. They’re performed with the context of previous transactions and the current transaction may be affected by what happened during previous transactions. For these reasons, stateful apps use the same servers each time they process a request from a user.  

    If a stateful transaction is interrupted, the context and history have been stored so you can more or less pick up where you left off. Stateful apps track things like window location, setting preferences, and recent activity. You can think of stateful transactions as an ongoing periodic conversation with the same person.

    In terms of authorization,
    - **Stateful** = save authorization info on server side, this is the traditional way
    - **Stateless** = save authorization info on client side, along with a signature to ensure integrity, in form of tokens
   
    **[⬆ Back to Top](#table-of-contents)**
    
---

## Django Rest Framework

1. ### What is Django Rest Framework?
   Django REST Framework is a web framework built over Django that helps to create web APIs which are a collection of URL endpoints containing available HTTP verbs that return JSON. It’s very easy to build model-backed APIs that have authentication policies and are browsable.
   
   **[⬆ Back to Top](#table-of-contents)**

2. ### What are benefits of using Django Rest Framework?
   - Its Web-browsable API is a huge usability win for your developers.
   - Authentication policies include packages for OAuth1 and OAuth2.
   - Serialization supports both ORM and non-ORM data sources.
   - It’s customizable all the way down. Just use regular function-based views if you don’t need the more powerful features.
   - It has extensive documentation and great community support.
   - It’s used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.
 
   **[⬆ Back to Top](#table-of-contents)**
 
 3. ### What are serializers?
    Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

    **[⬆ Back to Top](#table-of-contents)**
   
4. ### What are Permissions in DRF?
   Permission checks are always run at the very start of the view, before any other code is allowed to proceed. Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted.

   Permissions are used to grant or deny access for different classes of users to different parts of the API.

   The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user. This corresponds to the `IsAuthenticated` class in REST framework.

   These can be applied at a **project-level**, a **view-level**, or at any **individual model level**.

    **[⬆ Back to Top](#table-of-contents)**
    
5. ### How to add login in the browsable API provided by DRF?
   Within the project-level `urls.py` file, add a new URL route that includes `rest_framework.urls`.
   
   ```python
   # blog_project/urls.py
   from django.urls import include, path

   urlpatterns = [
   ...
   path('api-auth/', include('rest_framework.urls')), # new
   ]
   ```
    
    **[⬆ Back to Top](#table-of-contents)**

6. ### What are Project-Level Permissions?
   Django REST Framework ships with a number of built-in project-level permissions settings we can use, including:

   - **AllowAny** - any user, authenticated or not, has full access
   - **IsAuthenticated** - only authenticated, registered users have access
   - **IsAdminUser** - only admins/superusers have access
   - **IsAuthenticatedOrReadOnly** - unauthorized users can view any page, but only authenticated users have write, edit, or delete privileges

   Implementing any of these four settings requires updating the `DEFAULT_PERMISSION_CLASSES` setting:

    ```python
   # blog_project/settings.py

   REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.IsAuthenticated', # new
     ]
   }
   ```
    **[⬆ Back to Top](#table-of-contents)**

7. ### How to make custom permission classes?
   To make custom permission class, create a file named `permissions.py` that imports permissions at the top and then create your custom class, for example - `IsAuthorOrReadOnly` which extends `BasePermission`, then we override `has_object_permission`. 

    **[⬆ Back to Top](#table-of-contents)**
    
8. ### What is Basic Authentication?
   The most common form of HTTP authentication is known as “Basic” Authentication. When a client makes an HTTP request, it is forced to send an approved authentication credential before access is granted.

   The complete request/response flow looks like this:
   1. Client makes an HTTP request
   2. Server responds with an HTTP response containing a `401 (Unauthorized)` status code and `WWW-Authenticate` HTTP header with details on how to authorize
   3. Client sends credentials back via the `Authorization` HTTP header
   4. Server checks credentials and responds with either `200 OK` or `403 Forbidden` status code.
   Once approved, the client sends all future requests with the Authorization HTTP header credentials.

   > **Note:** The authorization credentials sent are the **unencrypted base64 encoded** version of `<username>:<password>`.

    **[⬆ Back to Top](#table-of-contents)**
    
9. ### What are the disadvantages of Basic Authentication?
   **Cons of Basic Authentication:**
   - On every single request the server must look up and verify the username and password, which is inefficient. 
   - User credentials are being passed in clear text—not encrypted at all, can be easily captured and reused.
   
    **[⬆ Back to Top](#table-of-contents)**
    
10. ### What is session authentication?
    At a high level, the client authenticates with its credentials (username/password) and then receives a _session ID_ from the server which is stored as a _cookie_). This session ID is then passed in the header of every future HTTP request. When the session ID is passed, the server uses it to look up a session object containing all available information for a given user, including credentials. This approach is **stateful** because a record must be kept and maintained on both the server (the session object) and the client (the session ID).

    Let’s review the basic flow:
    1. A user enters their log in credentials (typically username/password)
    2. The server verifies the credentials are correct and generates a session object that is then stored in the database
    3. The server sends the client a session ID — not the session object itself—which is stored as a cookie on the browser
    4. On all future requests the session ID is included as an HTTP header and, if verified by the database, the request proceeds
    5. Once a user logs out of an application, the session ID is destroyed by both the client and server
    6. If the user later logs in again, a new session ID is generated and stored as a cookie on the client

    > **Note:** The default setting in Django REST Framework is actually a combination of Basic Authentication and Session Authentication. Django’s traditional session-based authentication system is used and the session ID is passed in the HTTP header on each request via Basic Authentication.

    **[⬆ Back to Top](#table-of-contents)**

11. ### What are the pros and cons of session authentication?
    **Pros:**
    - User credentials are only sent once, not on every request/response cycle as in Basic Authentication. 
    - It is also more efficient since the server does not have to verify the user’s credentials each time, it just matches the session ID to the session object which is a fast look up.

    **Cons:**
    - A session ID is only valid within the browser where log in was performed; it will not work across multiple domains. This is an obvious problem when an API needs to support multiple front-ends such as a website and a mobile app. 
    - The session object must be kept up-to-date which can be challenging in large sites with multiple servers.
    - The cookie is sent out for every single request, even those that don’t require authentication, which is inefficient. 

    > **Note:** It is generally not advised to use a session-based authentication scheme for any API that will have multiple front-ends.
  
    **[⬆ Back to Top](#table-of-contents)**

12. ### What is Token Authentication?
    Tokens are pieces of data that carry just enough information to facilitate the process of determining a user's identity or authorizing a user to perform an action. All in all, tokens are artifacts that allow application systems to perform the authorization and authentication process.
    
    Token-based authentication is **stateless**: once a client sends the initial user credentials to the server, a unique token is generated and then stored by the client as either a cookie or in local storage. This token is then passed in the header of each incoming HTTP request and the server uses it to verify that a user is authenticated. The server itself does not keep a record of the user, just whether a token is valid or not.
    
    **[⬆ Back to Top](#table-of-contents)**
 
13. ### What are pros and cons of token authentication?
    **Pros:**
    - Since tokens are stored on the client, scaling the servers to maintain up-to-date session objects is no longer an issue.
    - Tokens can be shared amongst multiple front-ends: the same token can represent a user on the website and the same user on a mobile app.

    **Cons:**
    - A token contains all user information, not just an id as with a session id/session object set up. Since the token is sent on every request, managing its size can become a performance issue.

    **[⬆ Back to Top](#table-of-contents)**

14. ### What is the difference between cookies vs localStorage?
    - Cookies are used for reading server-side information. 
    - They are smaller (4KB) in size and automatically sent with each HTTP request. 

    - LocalStorage is designed for client-side information. 
    - It is much larger (5120KB) and its contents are not sent by default with each HTTP request.

    **[⬆ Back to Top](#table-of-contents)**

15. ### Where should token be saved - cookie or localStorage?
    With token-based auth, you are given the choice of where to store the JWT. Commonly, the JWT is placed in the browser's local storage and this works well for most use cases. There are some issues with storing JWTs in local storage to be aware of. Unlike cookies, local storage is sandboxed to a specific domain and its data cannot be accessed by any other domain including sub-domains.

    You can store the token in a cookie instead, but the max size of a cookie is only 4kb so that may be problematic if you have many claims attached to the token. Additionally, you can store the token in session storage which is similar to local storage but is cleared as soon as the user closes the browser.

    Tokens stored in both cookies and localStorage are vulnerable to XSS attacks. The current best practice is to store tokens in a cookie with the httpOnly and Secure cookie flags.

    **[⬆ Back to Top](#table-of-contents)**

16. ### What are disadvantages of Django REST Framework's built-in TokenAuthentication?
    - It doesn't support setting tokens to expire
    - It only generates one token per user
    
    **[⬆ Back to Top](#table-of-contents)**

17. ### What are JSON Web Tokens(JWTs)?
    JSON web token (JWT), is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
    
    Because of its relatively small size, a JWT can be sent through a URL, through a POST parameter, or inside an HTTP header, and it is transmitted quickly. A JWT contains all the required information about an entity to avoid querying a database more than once. The recipient of a JWT also does not need to call a server to validate the token.
    
    **[⬆ Back to Top](#table-of-contents)**
 
18. ### What are benefits of JWT?
    - **More compact:** JSON is less verbose than XML, so when it is encoded, a JWT is smaller than a simple token. This makes JWT a good choice to be passed in HTML and HTTP environments.

    - **More secure:** JWTs can use a public/private key pair for signing. A JWT can also be symmetrically signed by a shared secret using the HMAC algorithm.

    - **More common:** JSON parsers are common in most programming languages because they map directly to objects. 

    - **Easier to process:** JWT is used at internet scale. This means that it is easier to process on user's devices, especially mobile.

    **[⬆ Back to Top](#table-of-contents)**

19. ### What is the difference between a session and cookie?
    A cookie is a bit of data stored by the browser and sent to the server with every request.Cookies are used to identify sessions. A session is a collection of data stored on the server and associated with a given user (usually via a cookie containing an id code).

    The main difference between a session and a cookie is that session data is stored on the server, whereas cookies store data in the visitor’s browser. Sessions are more secure than cookies as it is stored in server. Cookie can be turned off from browser. Data stored in cookie can be stored for months or years, depending on the life span of the cookie. But the data in the session is lost when the web browser is closed. 

    **[⬆ Back to Top](#table-of-contents)**
    
20. ### What is the difference between cookie and tokens?
    Cookie-based authentication is stateful. This means that an authentication record or session must be kept both server and client-side. The server needs to keep track of active sessions in a database, while on the front-end a cookie is created that holds a session identifier, thus the name cookie based authentication.

    Token-based authentication is stateless. The server does not keep a record of which users are logged in or which JWTs have been issued. Instead, every request to the server is accompanied by a token which the server uses to verify the authenticity of the request. The token is generally sent as an addition Authorization header in the form of Bearer {JWT}, but can additionally be sent in the body of a POST request or even as a query parameter.

    > Read more [here](https://stackoverflow.com/questions/17000835/token-authentication-vs-cookies)

    **[⬆ Back to Top](#table-of-contents)**

21. ### What's an access token?
    When a user logins in, the authorization server issues an access token, which is an artifact that client applications can use to make secure calls to an API server. When a client application needs to access protected resources on a server on behalf of a user, the access token lets the client signal to the server that it has received authorization by the user to perform certain tasks or access certain resources.
    
    **[⬆ Back to Top](#table-of-contents)**

22. ### What is meant by a bearer token?
    A bearer token stands for a token that can be used by those who hold it. The access token thus acts as a credential artifact to access protected resources rather than an identification artifact. 

    **[⬆ Back to Top](#table-of-contents)**
    
23. ### What is the security threat to access token?
    Malicious users could theoretically compromise a system and steal access tokens, which in turn they could use to access protected resources by presenting those tokens directly to the server.

    As such, it's critical to have security strategies that minimize the risk of compromising access tokens. One mitigation method is to create access tokens that have a short lifespan: they are only valid for a short time defined in terms of hours or days.  

    **[⬆ Back to Top](#table-of-contents)**

24. ### What is a refresh token?
    For security purposes, access tokens may be valid for a short amount of time. Once they expire, client applications can use a refresh token to "refresh" the access token. That is, a refresh token is a credential artifact that lets a client application get new access tokens without having to ask the user to log in again.

    The client application can get a new access token as long as the refresh token is valid and unexpired. Consequently, a refresh token that has a very long lifespan could theoretically give infinite power to the token bearer to get a new access token to access protected resources anytime. The bearer of the refresh token could be a legitimate user or a malicious user.

    **[⬆ Back to Top](#table-of-contents)**

25. ### What are the best practices when using token authentication?
    Some basic considerations to keep in mind when using tokens:

    - Keep it secret. Keep it safe.
    - Do not add sensitive data to the payload.
    - Give tokens an expiration.
    - Embrace HTTPS.
    - Consider all of your authorization use cases.
    - Store and reuse.
    
    **[⬆ Back to Top](#table-of-contents)**

26. ### What is cookie-based authentication?
    A request to the server is always signed in by authorization cookie.
    **Pros:**
    - Cookies can be marked as "http-only" which makes them impossible to be read on the client side. This is better for XSS-attack protection.
    - Comes out of the box - you don't have to implement any code on the client side.
    
    **Cons:**
    - Bound to a single domain.
    - Vulnerable to XSRF. You have to implement extra measures to make your site protected against cross site request forgery.
    - Are sent out for every single request, (even for requests that don't require authentication).

    **[⬆ Back to Top](#table-of-contents)**

27. ### What are viewsets in DRF?
    A viewset is a way to combine the logic for multiple related views into a single class. In other words, one viewset can replace multiple views. It is a class that is simply a type of class-based View, that does not provide any method handlers such as `.get()` or `.post()`, and instead provides actions such as `.list()` and `.create()`.

    **[⬆ Back to Top](#table-of-contents)**
 
28. ### What are routers in DRF?
    Routers work directly with viewsets to automatically generate URL patterns for us. Django REST Framework has two default routers: SimpleRouter and DefaultRouter.
    - **SimpleRouter** - This router includes routes for the standard set of list, create, retrieve, update, partial_update and destroy actions.
    - **Default Router** - This router is similar to SimpleRouter, but additionally includes a default API root view, that returns a response containing hyperlinks to all the list views. It also generates routes for optional `.json` style format suffixes.

    **[⬆ Back to Top](#table-of-contents)**

29. ### What is the difference between APIViews and Viewsets in DRF?
    DRF has two main systems for handling views:

    - **`APIView`:** This provides methods handler for http verbs: get, post, put, patch, and delete.
    - **`ViewSet`:** This is an abstraction over `APIView`, which provides actions as methods:
      - **list:** read only, returns multiple resources (http verb: get). Returns a list of dicts.
      - **retrieve:** read only, single resource (http verb: get, but will expect an id in the url). Returns a single dict.
      - **create:** creates a new resource (http verb: post)
      - **update/partial_update:** edits a resource (http verbs: put/patch)
      - **destroy:** removes a resource (http verb: delete) 

     **[⬆ Back to Top](#table-of-contents)**

30. ### What is the difference between `GenericAPIView` and `GenericViewset`?
    - **`GenericAPIView`:** for APIView, this gives you shortcuts that map closely to your database models. Adds commonly required behavior for standard list and detail views. Gives you some attributes like, the `serializer_class`, also gives `pagination_class`, `filter_backend`, etc

    - **`GenericViewSet`:** There are many GenericViewSet, the most common being `ModelViewSet`. They inherit from `GenericAPIView` and have a full implementation of all of the actions: list, retrieve, destroy, updated, etc.

     **[⬆ Back to Top](#table-of-contents)**

