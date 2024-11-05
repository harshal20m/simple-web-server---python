Here's a README file for the **Simple Web Server** project that provides instructions, usage details, and embedded images. In a real scenario, you would add actual images of the running application, but here I'll describe placeholders so you can add them after testing.

---

# Simple Web Server

This project creates a simple web server using Python and Flask to simulate task execution, similar to job handling in Jenkins. The server allows you to start, stop, and check the status of tasks.

---

![Logo](https://user-images.githubusercontent.com/logo_placeholder.png)

---

## Table of Contents

-   [Features](#features)
-   [Getting Started](#getting-started)
-   [Endpoints](#endpoints)
-   [Example Usage](#example-usage)
-   [Screenshots](#screenshots)
-   [Contributing](#contributing)
-   [License](#license)

---

## Features

-   **Simulate Task Execution**: Start and stop tasks, like "build" and "test."
-   **Server Status Check**: View the current server status and tasks.
-   **Simple REST API**: Use HTTP requests to interact with the server.

---

## Getting Started

### Prerequisites

-   Python 3.7+
-   Flask

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/simple-web-server.git
    cd simple-web-server
    ```

2. Install Flask:
    ```bash
    pip install Flask
    ```

### Running the Server

Run the server with:

```bash
python simple_web_server.py
```

The server will start on `http://localhost:5000`.

---

## Endpoints

### 1. Home

-   **URL**: `/`
-   **Method**: GET
-   **Description**: Displays a welcome message.

### 2. Server Status

-   **URL**: `/status`
-   **Method**: GET
-   **Description**: Returns the server status and all task statuses.

### 3. Start Task

-   **URL**: `/start_task/<task_name>`
-   **Method**: POST
-   **Description**: Starts the specified task.
-   **Example**: `/start_task/build`

### 4. Stop Task

-   **URL**: `/stop_task/<task_name>`
-   **Method**: POST
-   **Description**: Stops the specified task.
-   **Example**: `/stop_task/build`

### 5. Task Status

-   **URL**: `/task_status/<task_name>`
-   **Method**: GET
-   **Description**: Checks the status of a specific task.
-   **Example**: `/task_status/build`

---

## Example Usage

1. **Home Page**: Open a browser and go to:

    ```
    http://localhost:5000/
    ```

    ![Home Page](https://user-images.githubusercontent.com/home_page_placeholder.png)

2. **Check Server Status**:

    ```
    curl http://localhost:5000/status
    ```

    ![Server Status](https://user-images.githubusercontent.com/server_status_placeholder.png)

3. **Start a Task** (e.g., `build`):

    ```
    curl -X POST http://localhost:5000/start_task/build
    ```

    ![Start Task](https://user-images.githubusercontent.com/start_task_placeholder.png)

4. **Stop a Task**:

    ```
    curl -X POST http://localhost:5000/stop_task/build
    ```

    ![Stop Task](https://user-images.githubusercontent.com/stop_task_placeholder.png)

5. **Check Specific Task Status**:
    ```
    curl http://localhost:5000/task_status/build
    ```
    ![Task Status](https://user-images.githubusercontent.com/task_status_placeholder.png)

---

## Screenshots

### Home Page

Shows a welcome message when accessing the server root.

![Home Page](https://user-images.githubusercontent.com/home_page_placeholder.png)

### Server Status

Displays server status and task list.

![Server Status](https://user-images.githubusercontent.com/server_status_placeholder.png)

### Task Started

Shows a response message after starting a ttask.

![Start Task](https://user-images.githubusercontent.com/start_task_placeholder.png)

---
