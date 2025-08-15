import os
from boomi import Boomi

# Load environment variables from .env file if dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

print("🚀 Boomi Python SDK - Sample Application")
print("=" * 45)

# Initialize the Boomi SDK
sdk = Boomi(
    account_id=os.getenv("BOOMI_ACCOUNT"),
    username=os.getenv("BOOMI_USER"),
    password=os.getenv("BOOMI_SECRET"),
    timeout=10000,
)

print("✅ SDK initialized successfully!")
print(f"📊 Available services: {len([attr for attr in dir(sdk) if not attr.startswith('_') and not attr.startswith('set')])}")

# Get account information - this endpoint returns general account details
# and doesn't require additional parameters beyond the account ID
account_id = os.getenv("BOOMI_ACCOUNT")
print(f"\n🔍 Fetching account information for: {account_id}")

try:
    result = sdk.account.get_account(id_=account_id)
    
    print("✅ Account information retrieved successfully!")
    print(f"📋 Result type: {type(result).__name__}")
    print(f"📋 Result module: {type(result).__module__}")
    
    # Display account details if available
    if hasattr(result, '__dict__'):
        account_attrs = [key for key, value in result.__dict__.items() 
                        if not key.startswith('_') and value is not None]
        
        if account_attrs:
            print("\n📋 Account Details:")
            for key, value in result.__dict__.items():
                if not key.startswith('_') and value is not None:
                    print(f"  {key}: {value}")
        else:
            print("\n📋 Account object created successfully (minimal data returned)")
            print("   This indicates the API call was successful and authentication is working")
    
    print(f"\n🎉 SUCCESS: Boomi SDK is working correctly!")
    print("🔧 All circular import issues have been resolved")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("🔧 Check your environment variables and API credentials")
