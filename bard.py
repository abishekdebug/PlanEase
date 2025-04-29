
import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")


# Create a config.
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")
# print(list(palm.list_models()))


# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day, members=1, package_type="bronze"):
    """
    Generate a personalized trip itinerary.
    
    Args:
        source (str): Starting location
        destination (str): Destination location
        start_date (str): Start date of the trip
        end_date (str): End date of the trip
        no_of_day (int): Number of days for the trip
        members (int): Number of travelers
        package_type (str): Type of package (bronze, gold, platinum)
        
    Returns:
        str: Generated itinerary text
    """
    # Define budget ranges based on package type
    budget_descriptions = {
        "bronze": "budget-friendly (economy class)",
        "gold": "mid-range (comfortable)",
        "platinum": "luxury (premium)"
    }
    
    # Get the budget description based on package type
    budget_desc = budget_descriptions.get(package_type, "budget-friendly")
    
    prompt = f"""Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} 
    from {start_date} to {end_date}, for {members} {'person' if members == 1 else 'people'}, 
    with a {budget_desc} budget (Currency:INR).
    
    Please include:
    1. Estimated overall budget
    2. Accommodation recommendations
    3. Daily activities and attractions
    4. Transportation options
    5. Restaurant suggestions
    6. Any special considerations for a group of {members} {'person' if members == 1 else 'people'}
    
    For a {package_type.upper()} package, focus on {'budget-friendly options' if package_type == 'bronze' else 'premium experiences' if package_type == 'platinum' else 'balanced quality and value'}.
    """
    
    response = model.generate_content(prompt)
    return(response.text)