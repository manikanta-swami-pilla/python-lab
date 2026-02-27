import random
import datetime
import os

# Define services, log levels, and message templates
services = [
    "AuthService", "PaymentGateway", "Database", "CacheService",
    "Security", "Scheduler", "API", "NotificationService"
]

levels = ["INFO", "WARN", "ERROR"]

messages = {
    "INFO": [
        "User login successful: user_id={id}",
        "Request processed: endpoint=/orders, status=200",
        "Job executed: job_id=reporting-{id}, duration={duration}s",
        "Notification sent: channel=email, user_id={id}"
    ],
    "WARN": [
        "Transaction latency high: txn_id={id}, duration={duration}ms",
        "Slow query detected: query=SELECT * FROM orders, duration={duration}ms",
        "Multiple failed login attempts: user_id={id}, count={count}",
        "Cache miss rate elevated: host=cache-prod-{id}, rate={rate}%"
    ],
    "ERROR": [
        "Connection failed: host=db-prod-{id}, error=timeout",
        "Redis unavailable: host=cache-prod-{id}, error=connection refused",
        "Payment declined: txn_id={id}, reason=insufficient funds",
        "Service crash detected: service={svc}, error=segfault"
    ]
}

def generate_log_line():
    # Random timestamp within the last ~3 days
    ts = datetime.datetime.now() - datetime.timedelta(
        minutes=random.randint(0, 5000)
    )
    timestamp = ts.strftime("%Y-%m-%d %H:%M:%S")
    service = random.choice(services)
    level = random.choice(levels)
    template = random.choice(messages[level])
    msg = template.format(
        id=random.randint(1000, 9999),
        duration=random.randint(100, 5000),
        count=random.randint(1, 10),
        rate=random.randint(1, 100),
        svc=random.choice(services)
    )
    return f"{timestamp} {level} {service} - {msg}"

def main():
    os.makedirs("data", exist_ok=True)
    filepath = "data/sample_logs.txt"
    with open(filepath, "w") as f:
        for _ in range(100):   # ✅ changed from 1000 to 100
            f.write(generate_log_line() + "\n")
    print(f"Generated {filepath} with 100 log lines")

if __name__ == "__main__":
    main()