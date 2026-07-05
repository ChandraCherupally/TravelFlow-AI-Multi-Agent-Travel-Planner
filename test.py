from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import get_database_url, run_travel_agent
#res = tavily_search("Best hotels in India")
#print(res)

#res = search_flights("Plan a 7 days Japan trip from Delhi")
#print(res)

#print(get_database_url())

#Plan a complete 7 days Japan trip from India including flights, hotels and sightseeing under 2 lakh INR
user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFinal response:\n")
print(response["answer"])