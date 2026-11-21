transactions = [    {"id": 101, "amount": 5000, "status": "success"},    {"id": 102, "amount": 2000, "status": "failed"},    {"id": 103, "amount": 8000, "status": "success"},    {"id": 104, "amount": 1500, "status": "pending"},    {"id": 105, "amount": 3000, "status": "success"},    {"id": 106, "amount": 1000, "status": "failed"}]

failed_count=0
pending_count=0
success_count=0
total_success_trans_amt=0
for transactions in transactions:
    status=transactions["status"]
    id=transactions["id"]
    amount=transactions["amount"]
    if status=="success":
        print(f"id: {id}, ", end="")
        print(f"amount: {amount}, ",end="")
        print(f"Status: {status} ",end="\n")
        success_count+=1
        total_success_trans_amt+=amount
    elif status=="failed":
        failed_count+=1
        continue
    else:
        pending_count+=1
        continue

print("Transaction Report")
print(f"Total Transactions {success_count+failed_count+pending_count}")
print(f"Total Success Transaction: {success_count}")
print(f"Total failed Transaction: {failed_count}")
print(f"Total Pending Transaction: {pending_count}")
print(f"Total Sucess trans amount: {total_success_trans_amt}")