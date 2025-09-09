# Assignment 2 – UDP Socket Programming (UDP Pinger Simulation)

This project is a **simulation of UDP socket programming** developed for the **Computer Networks** course.  
It models client–server communication with **custom Python classes** (`Serverdata`, `Clientmy`) instead of the actual `socket` library, focusing on **logic, validation, and message handling**.  

---

## 📖 Project Overview
- The server and client are implemented in **main.py**.  
- **Serverdata** validates domain/type/protocol numbers, accepts connections on port `9000`, and processes client messages.  
- **Clientmy** connects to the server, sends messages, and handles server responses.  
- The program simulates **UDP Pinger behavior** by checking round-trip times (RTT) using predefined message types.  

---

## ⚙️ Features

### 🔹 Serverdata Class
- `socketcreator(domain, type, protocol)`  
  - Accepts values `4-1-1` only.  
  - Returns success if valid, otherwise prints error and exits.  
- `serveraccept(client_port)`  
  - Accepts connection only if port = **9000**.  
- `serverreader(message)`  
  - Handles client messages:  
    - `Access5000` → RTT accepted (low)  
    - `Access9000` → RTT high warning  
    - `end` → closes the server  
    - Other → Access Denied  

### 🔹 Clientmy Class
- `clientcreator(domain, type, protocol)` → Validates 4-1-1  
- `clientconnect()` → Requests port number (input)  
- `clientwriter(server)` → Sends user input messages, processes server feedback  

---

## 📡 Supported Messages
- `Access5000` → Accepted, RTT low  
- `Access9000` → Accepted, RTT high  
- `Hello`, `There_is_no_answer` → Access Denied  
- `end` → Ends server connection  

---

## 🖥️ How to Run
1. Make sure you have **Python 3.8+** installed.  
2. Run the program:  
   ```bash
   python main.py
   ```
3. Enter the required values when prompted:  
   - Domain number → `4`  
   - Type number → `1`  
   - Protocol number → `1`  
   - Port number → `9000`  
4. Send messages (`Access5000`, `Access9000`, `Hello`, `end`) and observe server responses.  

---

## 📂 File Structure
```
Assignment2/
│── main.py        # Contains Serverdata and Clientmy classes
│── Report.pdf     # Detailed report explaining program flow and test cases
│── README.md      # Project documentation
```

---

## 📸 Example Outputs
- **Valid connection**  
  ```
  Enter domain number: 4
  Enter type number: 1
  Enter protocol number: 1
  Server: Server is created
  Server: Server is listening
  Client: Client is created
  Client: Client is ready to connection
  Client: Send connection demand to the server
  Client: Enter the port number: 9000
  Server: Connected to the server
  ```
- **Access5000 message**  
  ```
  Server: Message is Access5000 access permitted
  Client: Round Trip Time can be accepted.
  ```
- **Access9000 message**  
  ```
  Server: Message is Access9000 access permitted
  Client: Round Trip Time is high. Check internet connection.
  ```
- **end message**  
  ```
  Server: Server closed
  ```

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **Simulation of UDP sockets** – No real network connection  

---

## 🎓 Note
This project was developed as part of the **CMPE 472 – Computer Networks** course.  
It is a **simulation assignment** and does **not use the Python socket library**.  
