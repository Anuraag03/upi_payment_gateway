# UPI Payment System 💸

A simulated UPI (Unified Payments Interface) banking system built with **Python**, leveraging **SQLite**, and **socket programming**. It replicates core functionality of UPI transactions between **Users**, **Merchants**, and **Banks** across a shared LAN.

---

## 🧱 Architecture

This project consists of **3 key components**:

1. **Bank Server (`bank.py`)**  
   Hosts all banks and handles user/merchant registrations, validations, and balance updates.

2. **UPI Machine (`upi_machine.py`)**  
   Acts as the central node for merchant registration and QR/VMID-based transaction initiation.

3. **User Client (`user_client.py`)**  
   Used by customers to register and perform UPI transactions using MMID and VMID.

---

## 🧪 Features

### ✅ User
- Register with a bank branch using name, IFSC, mobile, password, and UPI PIN.
- Receive a **UID** and **MMID** (generated via SHA256).
- Perform transactions using Merchant VMIDs.

### ✅ Merchant
- Register via the UPI Machine with name, IFSC, and password.
- Receive a **MID** (Merchant ID) — 16-digit hexadecimal string.
- Generate a **VMID** by encrypting the MID using the **SPECK cipher**.
- VMID is encoded in a QR Code for transaction initiation.

### ✅ Transaction
- User provides MMID, PIN, and Merchant VMID.
- UPI Machine forwards the transaction to the appropriate Bank Server.
- If verified, funds are transferred from User to Merchant.

---

## ⚙️ How to Run

### 1️⃣ Setup

- Python 3.8+
- Install required packages: qrcode , pillow

```bash
pip install -r requirements.txt
```


### 2️⃣ Start the Bank Server

Run each component in a different terminal
Run the following command:

```bash
python bank.py
```

This will launch the Bank Server which supports multiple banks like HDFC, SBI, and ICICI.


### 3️⃣ Register a Merchant (via UPI Machine)

Replace the IP addresses in the user.py and upi_machine.py with your LAN IP address, you can check IP address by running ipconfig(windows)/ifconfig(Linux/Mac)
Run the following command:
Update the BANK_SERVER_IP with the IP of the device running the bank.py script.

```bash
python upi_machine.py
```

Choose option `1`:

```plaintext
1. Register a Merchant
2. Generate QR Code for UPI Transactions
```

After registration, choose option `2` and enter your MID to generate a VMID and QR code for transactions.

### 4️⃣ Register and Transact as User

Run the following command:
Update the BANK_SERVER_IP with the IP of the device running the bank.py script.
Update the UPI_MACHINE_HOST with the IP of the device running the upi_machine.py script
```bash
python user_client.py
```

Choose:

1. To register as a user.  
2. To initiate a transaction:

- Enter your MMID.
- UPI PIN.
- Merchant’s VMID (from QR).
- Amount to pay.

If successful, you’ll see the response from the bank.

---
### 4️⃣ Bank Dashboard

Run 
```bash
python bank_dashboard.py
```

After you have registered users , merchants and performed transactions to see the list of users , merchants and thier details

---

### 4️⃣ Blockchain Logging

Run 
```bash
python view_blockchains.py
```

Transactions are logged in Centralized Blockchain Ledgers for each Bank , These transactions per bank can be viewed by running the above script.

---



## 💡 Notes
- Replace the IP addresses before running the scripts
- All sockets run over LAN (use private IPs like `192.168.x.x` or `172.x.x.x`).
- Ensure firewalls allow connections to ports `8000` and `9001`.
- Each entity (user, merchant) is linked to a specific bank via IFSC code.

---
