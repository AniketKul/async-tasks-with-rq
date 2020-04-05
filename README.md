# Asynchronous Tasks with Flask and Redis Queue

If a long-running task is part of your application's workflow you should handle it in the background, outside the normal flow.

## Problem Statement

Suppose your web application requires users to submit a thumbnail (which will probably need to be re-sized) and confirm their email when they register. If your application processed the image and sent a confirmation email directly in the request handler, then the end user would have to wait for them both to finish. Instead, you'll want to pass these tasks off to a task queue and let a separate worker process deal with it, so you can immediately send a response back to the client. The end user can do other things on the client-side and your application is free to respond to requests from other users.


## Quick Start

1] First step is to build the custom `web` image on your local using docker-compose

```
$ docker-compose build
```

2] Run the built image

```
$ docker-compose up -d --build
```

Open your browser to http://localhost:5004 to view the app and/or http://localhost:9181 to view the RQ dashboard.
