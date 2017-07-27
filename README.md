# github-traffic-stats-collector

WORK IN PROGRESS

## Architecture

### Diagram

```text
                          +---------------+
                          | +-----------+ |
                          | | Database  | | --------+
                          | +-----------+ | <-----+ |
                          |               |   GH  | | DB Processing
            Cron Trigger  |               | Stats | |    Trigger
+--------+ <------------- | +-----------+ | ------+ |
| GitHub |                | | OpenWhisk | | <-------+
+--------+ -------------> | +-----------+ | ------+
           Traffic Stats  |               |       |
                          |               |       | Update Dashboard
                          | +-----------+ |       |
                          | | Dashboard | | <-----+
                          | +-----------+ |
                          +---------------+
```

### Chronology

1. OpenWhisk cron trigger sends request for traffic statistics to GitHub
2. GitHub Returns traffic statistics
3. OpenWhisk sends GitHub Statistics to database
  * If database receives new statistics:
    1. Trigger OpenWhisk to process data
    2. Send newly processed data to dashboard
4. Dashboard displays reports
