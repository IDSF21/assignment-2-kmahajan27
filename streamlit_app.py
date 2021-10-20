import streamlit as st
import numpy as np
import pandas as pd
from pandas import json_normalize
import altair as alt
from vega_datasets import data
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2, country_alpha3_to_country_alpha2, country_alpha2_to_country_name
# from geopy.geocoders import Nominatim
import time
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


st.title("Hotel Booking Demand Data")

df = pd.read_csv ('hotel_bookings_mod1.csv')


def draw_map():
    df_country_count = df.groupby('country2', as_index = False).agg(countpercountry = ( "country2", "count"))
    print('len(df_country_count): ', len(df_country_count))
    df_country_count['country_code'] = df_country_count["country2"]
    df_country_count['country_name'] = df_country_count['country2']


    for i in range(len(df_country_count)):
        df_country_count['country_code'][i] = df_country_count["country2"][i][2:4]

    for i in range(len(df_country_count)):
        try:
            df_country_count['country_name'][i] = country_alpha2_to_country_name(df_country_count["country_code"][i])   
        except:
            df_country_count['country_name'][i] = 'Unknown' 


    country_codes = pd.read_csv('country_codes.csv',sep=',', encoding='latin-1')
    # print(country_codes)
    
    for i in range(len(country_codes['Alpha-2 code'])):
        if(country_codes['Alpha-2 code'][i] not in df_country_count['country_code'].values):
            df_country_count = df_country_count.append({'country_code': country_codes['Alpha-2 code'][i], 'country2':'', 'countpercountry': 0, 'country_name': country_codes['English short name'][i]}, ignore_index = True)

    
    country_codes.set_index('Alpha-2 code', inplace = True)
    df_country_count.set_index('country_code', inplace = True)
    df_country_count['id'] = country_codes['Numeric']
    
    # print(df_country_count)

            
    COLOR_THEME = {'Total':"lightgreyred"}
    
#     df_country_count['count']

    source = alt.topo_feature(data.world_110m.url, "countries")
    # print(source)
    world_map = (
        alt.Chart(source, title='Countries of Travellers by Number of Hotel Bookings')
        .mark_geoshape(stroke="black", strokeWidth=0.15)
        .encode(
            color=alt.Color(
                "countpercountry:N", 
                scale=alt.Scale(scheme="lightgreyred"), 
                legend=None),
            tooltip=[
                alt.Tooltip("country_name:N", title="Country"),
                alt.Tooltip("countpercountry:Q", title="Hotel Bookings"),
            ],
        ).transform_lookup(
            lookup="id",
            from_=alt.LookupData(df_country_count, "id", ["country_name", "countpercountry"]),
        )
    ).configure_view(strokeWidth=0).properties(width=700, height=400).project("naturalEarth1")
    
    return world_map



def draw_map_year(select_years):
    df['arrival_date_year'] = df['arrival_date_year'].astype(str)
    df_country_count = df[df['arrival_date_year'].isin(select_years)]
    df_country_count = df_country_count.groupby('country2', as_index = False).agg(countpercountry = ( "country2", "count"))
    df_country_count['country_code'] = df_country_count["country2"]
    df_country_count['country_name'] = df_country_count['country2']


    for i in range(len(df_country_count)):
        df_country_count['country_code'][i] = df_country_count["country2"][i][2:4]

    for i in range(len(df_country_count)):
        try:
            df_country_count['country_name'][i] = country_alpha2_to_country_name(df_country_count["country_code"][i])   
        except:
            df_country_count['country_name'][i] = 'Unknown' 


    country_codes = pd.read_csv('country_codes.csv',sep=',', encoding='latin-1')
    
    for i in range(len(country_codes['Alpha-2 code'])):
        if(country_codes['Alpha-2 code'][i] not in df_country_count['country_code'].values):
            df_country_count = df_country_count.append({'country_code': country_codes['Alpha-2 code'][i], 'country2':'', 'countpercountry': 0, 'country_name': country_codes['English short name'][i]}, ignore_index = True)

    country_codes.set_index('Alpha-2 code', inplace = True)
    df_country_count.set_index('country_code', inplace = True)

    df_country_count['id'] = country_codes['Numeric']
    # print(len(df_country_count))

    COLOR_THEME = {'Total':"lightgreyred"}
    
#     df_country_count['count']

    source = alt.topo_feature(data.world_110m.url, "countries")
    # print(source)
    world_map = (
        alt.Chart(source, title='Countries of Travellers by Number of Hotel Bookings')
        .mark_geoshape(stroke="black", strokeWidth=0.15)
        .encode(
            color=alt.Color(
                "countpercountry:N", 
                scale=alt.Scale(scheme="lightgreyred"), 
                legend=None),
            tooltip=[
                alt.Tooltip("country_name:N", title="Country"),
                alt.Tooltip("countpercountry:Q", title="Hotel Bookings"),
            ],
        )
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(df_country_count, "id", ["country_name", "countpercountry"]),
        )
    ).configure_view(strokeWidth=0).properties(width=700, height=400).project("naturalEarth1")
    
    return world_map



def draw_map_month(select_months):
    df['arrival_date_month'] = df['arrival_date_month'].astype(str)
    df_country_count = df[df['arrival_date_month'].isin(select_months)]
    df_country_count = df_country_count.groupby('country2', as_index = False).agg(countpercountry = ( "country2", "count"))
    df_country_count['country_code'] = df_country_count["country2"]
    df_country_count['country_name'] = df_country_count['country2']


    for i in range(len(df_country_count)):
        df_country_count['country_code'][i] = df_country_count["country2"][i][2:4]

    for i in range(len(df_country_count)):
        try:
            df_country_count['country_name'][i] = country_alpha2_to_country_name(df_country_count["country_code"][i])   
        except:
            df_country_count['country_name'][i] = 'Unknown' 


    country_codes = pd.read_csv('country_codes.csv',sep=',', encoding='latin-1')
    
    for i in range(len(country_codes['Alpha-2 code'])):
        if(country_codes['Alpha-2 code'][i] not in df_country_count['country_code'].values):
            df_country_count = df_country_count.append({'country_code': country_codes['Alpha-2 code'][i], 'country2':'', 'countpercountry': 0, 'country_name': country_codes['English short name'][i]}, ignore_index = True)

    country_codes.set_index('Alpha-2 code', inplace = True)
    df_country_count.set_index('country_code', inplace = True)

    df_country_count['id'] = country_codes['Numeric']
    # print(df_country_count)

    COLOR_THEME = {'Total':"lightgreyred"}
    
#     df_country_count['count']

    source = alt.topo_feature(data.world_110m.url, "countries")
    # print(source)
    world_map = (
        alt.Chart(source, title='Countries of Travellers by Number of Hotel Bookings')
        .mark_geoshape(stroke="black", strokeWidth=0.15)
        .encode(
            color=alt.Color(
                "countpercountry:N", 
                scale=alt.Scale(scheme="lightgreyred"), 
                legend=None),
            tooltip=[
                alt.Tooltip("country_name:N", title="Country"),
                alt.Tooltip("countpercountry:Q", title="Hotel Bookings"),
            ],
        )
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(df_country_count, "id", ["country_name", "countpercountry"]),
        )
    ).configure_view(strokeWidth=0).properties(width=700, height=400).project("naturalEarth1")
    
    return world_map

st.subheader('What is the trend for travellers from different countries through the different years or the various months of the year?')


st.markdown("We aim to analyze if there is a seasonal trend to travellers from different countries. For example, say a country like Canada, we have a hypothesis that \
		that there would be more travellers in the summer months of November, December, January and February when it gets really cold in Russia, since people are looking for \
		respite from cold weather. Also, we are looking to find if there are particular years when there were more travellers from a country. We see that the hypothesis is not quite true. ")

with st.expander("See explanation"):
    st.subheader('Hypothesis Explanation')

    st.markdown("There are other more powerful factors governing the most popular months for travel. We find that travellers from most countries like United States, Russia, Brazil, France etc. prefer to travel in the summer months of April, May, June, and July. \
            A possible explanation for this is that children have school vacations during that time and so families are able to travel together. Another noticeable trend is that contrary to our hypothesis, December and January \
            which are generally the coldest months have least travellers. A possible explanation for this is that December and January are christmas and new year months. Hence, there are very few business travellers \
            and people prefer to spend time at home with their families. Also, we find that there is much less data for the year 2015 compared to the years 2016 and 2017. For the years, 2016 and 2017, the number of travellers are more or less similar \
            across countries.")


MODE = st.radio('Select Analysis Category',['All','Years','Months'])

if MODE == 'All':
    st.write(draw_map())
    
elif MODE == 'Years':
    
    select_years = st.multiselect('Select the Years',
               ['2015','2016','2017'],
               ['2017'])
    
    #display the map
    st.write(draw_map_year(select_years))
    
    # display(draw_map_year(select_years))
    #display the datatable below the map
#     st.table(olympic_medal_map.reset_index().set_index('Team/NOC')[['Medals']].sort_values(by='Medals', ascending=False))

elif MODE == 'Months':
    
    #add select option for countries with multiple choice. Default values would be Japan, ROC and Sweden
    select_months = st.multiselect('Select the months',
               ['January','Febraury','March','April','May','June','July','August','September','October','November','December'],
               ['January'])
    

    st.write(draw_map_month(select_months))
#     COUNTRY = st.multiselect('Select a team',
#                list(medal_count_by_gender['Team/NOC'].drop_duplicates().values),
#                             ['Japan','ROC','Sweden'])
    
#     #display the graph and table with the results
#     st.write(medals_by_gender(COUNTRY))
#     st.write('Medals won by selected countries')
#     st.table(medal_count_by_gender.loc[medal_count_by_gender['Team/NOC'].isin(COUNTRY),['Team/NOC','Medal type','count_female','count_male']])


st.subheader('How does the length of stay vary depending on the number of adults and children who are travelling together?')
st.markdown("Our aim is to analyze if there is a correlation between length of stay and number of adults and children travelling together. Typically \
            we expect that the length of stay will be longer when a person is travelling with family ie. with more adults and children compared to when \
            he/she is travelling alone.")

with st.expander("See explanation"):
    st.subheader('Hypothesis Explanation')

    st.markdown("From the data we find that when only 1 adult is traveling, the stay nights are less than 3 for over 60% of the observations. As the number increases to 3 adults, less than 30% of the observations correspond to less than 3 night stays.\
    			These results are for when there are no children. It indicates that groups tend to travel for longer length compared to single adults. With 1 child and 1 adult, more than 70% of the stays are 3 days or longer. With 3 children and 1 adult, more than 75% of the stays are 5 days or longer.\
    			Similar trend is seen with 2 adults and 1 child, and 2 adults and 2 children. With 1 child and 2 adults, around 67.5% of stays are 3 nights or more, while with 2 adults and 2 children, around 67.5% of stays are 3 nights or more.")


adult_value = st.slider("Select the number of adults", 0, 5)
child_value = st.slider("Select the number of children", 0, 3)

df['total_night_stays'] = df['stays_in_week_nights'] + df['stays_in_weekend_nights']
# print(df['children'])
def get_count(series, limit=None):
    
    '''
    INPUT:
        series: Pandas Series (Single Column from DataFrame)
        limit:  If value given, limit the output value to first limit samples.
    OUTPUT:
        x = Unique values
        y = Count of unique values
    '''
    
    if limit != None:
        series = series.value_counts()[:limit]
    else:
        series = series.value_counts()
    
    x = series.index
    y = series/series.sum()*100
    
    return x.values,y.values

def plot(x, y, x_label=None,y_label=None, title=None, figsize=(7,5), type='bar'):
    
    '''
    INPUT:
        x:        Array containing values for x-axis
        y:        Array containing values for y-axis
        x_lable:  String value for x-axis label
        y_lable:  String value for y-axis label
        title:    String value for plot title
        figsize:  tuple value, for figure size
        type:     type of plot (default is bar plot)
        
    OUTPUT:
        Display the plot
    '''
    
    sns.set_style('darkgrid')
    
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    
    if x_label != None:
        ax.set_xlabel(x_label)
    
    if y_label != None:
        ax.set_ylabel(y_label)
        
    if title != None:
        ax.set_title(title)
    
    if type == 'bar' and len(x)>0 and len(y)>0:
        sns.barplot(x,y, ax = ax)
    elif type == 'line' and len(x)>0 and len(y)>0:
        sns.lineplot(x,y, ax = ax, sort=False)
    
    st.write(fig)
    # plt.show()
    

df_stay_subset = df[df['adults'] == adult_value]
df_stay_subset = df_stay_subset[df_stay_subset['children'] == child_value]
# print(df_stay_subset['children'])

# if(len(df_stay_subset) == 0):
    
    
x,y = get_count(df_stay_subset['total_night_stays'], limit=10)

plot(x,y, x_label='Total Number of Nights', y_label='Booking Percentage (%)', title='Total Night Stay Duration (Top 10)', figsize=(10,5))


st.subheader('What is the trend of cancellations with respect to the number of days before which a reservation is made?')
st.markdown("Here, our aim is to analyze if there is a correlation between the booking gap (ie. the number of days between reservation and arrival) and the cancellations. Typically \
            we expect that the earlier someone has booked a stay, the more likely they are to cancel it due to emergence of unknown circumstances. In this graph, \
            we also stack the data based on various other variables - customer type, hotel. These variables give us more insight into the cancellations - for example, customer types \
            that are 'groups' seem to be less likely to cancel a reservation if its nearer to their arrival date than if its farther.")

            

with st.expander("See explanation"):
    st.subheader('Hypothesis Explanation')

    st.markdown("From this dataset, we find out that maximum cancellations are done if the time frame between reservation and arrival date is shorter. \
        Typically, we would expect people to cancel if their arrival dates are farther away. But that is not what we observe from this data, thus proving our hypothesis wrong. From the graph, we can also observe that transient customers are more prone to cancel their reservations. We expect this, because transient customers are not a part of any group or contract and so they are more likely to change their mind and cancel their reservations. Next, we observe that city hotels had more cancellations compared to resorts. This is again typical because city hotels have more business travellers, whose plans may change. Whereas, resort bookings are usually planned vacations, hence less likely to be cancelled.")

df_cancelled = df[df['is_canceled'] == 1]

CHOICES = {"customer_type": "Customer Type", "hotel" :"Hotel Type"}


def format_func(option):
    return CHOICES[option]

option = st.selectbox('Stack by?', options=list(CHOICES.keys()), format_func=format_func)
# st.subheader('(zoom in/out to change the range of the bins)')
brush = alt.selection_interval(bind='scales', encodings=['x'])
st.text('(zoom in/out to change the granularity of the graph or the width of the bins)')
chart = alt.Chart(df_cancelled).mark_bar().encode(
    y=alt.Y('count()', title="Frequency in lead time bins - cancelled reservations only"),
    x=alt.X('lead_time', bin=alt.Bin(maxbins=30, extent=brush), title="Lead time (bins)"),
    color = option
).properties(
    width=600,
    height=600
).add_selection(brush)


st.altair_chart(chart)
