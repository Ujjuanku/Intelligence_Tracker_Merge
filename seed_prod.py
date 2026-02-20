import asyncio
import httpx
import sys

# CONFIGURATION
# Set your production URL here
API_BASE_URL = "https://web-production-035fb.up.railway.app"

# Competitors to Add (Tech/SaaS Focus)
COMPETITORS = [
    "https://stripe.com/pricing",
    "https://auth0.com/pricing",
    "https://vercel.com/pricing",
    "https://railway.app/pricing",
    "https://openai.com/pricing",
    "https://www.anthropic.com/pricing"
]

async def seed_data():
    print(f"🚀 Seeding Production Data to: {API_BASE_URL}\n")
    
    async with httpx.AsyncClient() as client:
        # 1. Check if backend is reachable
        try:
            resp = await client.get(f"{API_BASE_URL}/")
            if resp.status_code != 200:
                print(f"❌ Backend seems down (Status: {resp.status_code})")
                return
            print("✅ Backend is reachable.")
        except Exception as e:
            print(f"❌ Could not connect: {e}")
            return

        # 2. Add Competitors
        print("\nAdding Competitors...")
        for url in COMPETITORS:
            try:
                # Add
                resp = await client.post(f"{API_BASE_URL}/competitors", data={"url": url})
                if resp.status_code in [200, 303]:
                    print(f"  ✅ Added: {url}")
                else:
                    print(f"  ⚠️ Failed to add {url}: {resp.status_code}")
                
                # Small delay to be polite
                await asyncio.sleep(1) 
            except Exception as e:
                print(f"  ❌ Error adding {url}: {e}")

        # 3. Fetch IDs to trigger 'Check Now'
        print("\nFetching IDs to run initial checks...")
        try:
            resp = await client.get(f"{API_BASE_URL}/api/competitors")
            competitors = resp.json()
            
            for comp in competitors:
                print(f"  Running Check for {comp['name']} (ID: {comp['id']})...")
                # Trigger Check
                check_resp = await client.post(f"{API_BASE_URL}/check/{comp['id']}")
                if check_resp.status_code in [200, 303]:
                    print(f"    ✅ Check complete for {comp['name']}")
                else:
                    print(f"    ⚠️ Check failed for {comp['name']}")
                
                # Wait to avoid hitting rate limits or timeouts
                await asyncio.sleep(2)
                
        except Exception as e:
            print(f"❌ Error fetching competitors: {e}")

    print("\n✨ Seeding Complete! Refresh your Dashboard.")

if __name__ == "__main__":
    asyncio.run(seed_data())
