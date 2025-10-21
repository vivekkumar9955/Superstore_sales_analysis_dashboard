def kpi_total_sales(data):
    return round(data['Sales'].sum(),1)

def kpi_tatal_profit(data):
    return round(data['Profit'].sum(),1)

def kpi_top_category(data):
    top_category = (
        data.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )
    return top_category

#filter region wise states
def get_states_by_region(selected_region, df):
    """
    Returns a list of states filtered by the selected region.

    Parameters:
        selected_region (str): The selected region name.
        df (pd.DataFrame): The DataFrame containing 'Region' and 'State' columns.

    Returns:
        list: ['Choose an option', ...states belonging to the region...]
    """
    # Handle the case when no region is selected
    if selected_region == "Choose an option":
        return ["Choose an option"] + sorted(df["State"].dropna().unique().tolist())

    # Filter states for the selected region
    filtered_states = (
        df.loc[df["Region"] == selected_region, "State"]
        .dropna()
        .unique()
        .tolist()
    )

    return ["Choose an option"] + sorted(filtered_states)

#filter city state wise
def get_city_by_states(selected_state , df):
    if selected_state == 'Choose an option':
        return ['Choose an option'] +sorted(df['City'].dropna().unique().tolist())

    #Filter city for the selected state

    filter_city = (
        df.loc[df['State'] == selected_state ,'City']
        .dropna()
        .unique()
        .tolist()
    )

    return ['Choose an option'] +sorted(filter_city)


def state_abbrev():
    # --- Map State names to abbreviations ---
    state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
        'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
        'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
        'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
        'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
        'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    return state_abbrev


