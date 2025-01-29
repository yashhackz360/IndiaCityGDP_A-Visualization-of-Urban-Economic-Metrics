import streamlit as st
import plotly.express as px
import pandas as pd
import smtplib
import openai




st.markdown("""

    <h1 style="background-color: #00FFFF; color: black; font-size: 40px; text-align: center;">Project : IndiaCityGDP</h1>

""", unsafe_allow_html=True)



# for Gdp Metrics page
# Gdp  data
Gdp_data =     {
    'City': ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata', 'Mumbai', 'Pune'],
    'Average GDP (in billion $)': [77.33, 128.50, 87.43, 102.33, 100.00, 34.83, 51.17, 360.00, 58.25]
}
df_Gdp = pd.DataFrame(Gdp_data)

# Gdp per capita data
Gdp_per_capita = {
    
    'City': ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata', 'Mumbai', 'Pune'],
    'Average GDP per Capita (in $)': [4000.00, 3548.33, 4048.33, 5034.83, 3541.67, 1950.00, 2250.00, 3600.00, 2950.00]
}
df_Gdp_per_capita = pd.DataFrame(Gdp_per_capita)


# for  sector metrics page 
# sector wise data
Sector_data = {
    'Year': [2019, 2020, 2021, 2022, 2023,2024],
    'Agriculture': [13.35666667, 12.34666667, 11.84, 11.98666667, 12.55,10.55],
    'Industrial': [18.0, 18.5, 19.0, 19.3, 19.5,19.0],
    'ICT': [17.76666667, 14.63333333, 15.95666667, 15.06666667, 14.94666667,14.99],
    'Tourism': [7.54, 6.796666667, 6.686666667, 7.246666667, 6.726666667,15.22],
    'Services': [26.44, 28.63, 24.92666667, 29.21666667, 25.92666667,26.4455]
}
df_sector = pd.DataFrame(Sector_data)


# For employment rates page
# Year-wise Unemployment data
employment_data = {
    'Year': [2019, 2020, 2021, 2022, 2023,2024],
    'Unemployment Rate': [6.66,6.41,5.28,6.03,6.13,6.08 ]
}
df_Unemployment = pd.DataFrame(employment_data)

#for R and D ,patents page
#Avg R & D ,patents Data
Avg_data = {

    'City': ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata', 'Mumbai', 'Pune'],
    'Average R&D Expenditure (% of GDP)': [1.23, 1.23, 0.93, 1.12, 1.02, 0.87, 1.14, 1.07, 1.07],
    'Average Patents per 100,000 Inhabitants': [4.0, 4.0, 3.0, 4.5, 3.5, 3.2, 4.0, 4.0, 3.5]
}
df_Rdpatents = pd.DataFrame(Avg_data)

# Dictionary containing the average values for each city
city_data = {
    "Ahmedabad": {"GDP": 80.67, "GDP per capita": 3750, "R&D Expenditure": 1.25, "Patents": 4.54},
    "Bengaluru": {"GDP": 124.67, "GDP per capita": 3748.33, "R&D Expenditure": 1.01, "Patents": 4.04},
    "Chennai": {"GDP": 89.33, "GDP per capita": 3874, "R&D Expenditure": 0.85, "Patents": 3.05},
    "Delhi": {"GDP": 127.67, "GDP per capita": 5037.67, "R&D Expenditure": 1.51, "Patents": 5.63},
    "Hyderabad": {"GDP": 91.67, "GDP per capita": 3833.33, "R&D Expenditure": 1.1, "Patents": 2.3},
    "Jaipur": {"GDP": 40.0, "GDP per capita": 2000, "R&D Expenditure": 1.2, "Patents": 3.01},
    "Kolkata": {"GDP": 50.0, "GDP per capita": 2500, "R&D Expenditure": 0.87, "Patents": 2.78},
    "Mumbai": {"GDP": 393.0, "GDP per capita": 3890, "R&D Expenditure": 1.29, "Patents": 6.71},
    "Pune": {"GDP": 63.0, "GDP per capita": 3180, "R&D Expenditure": 1.5, "Patents": 3.67}
    }


# Custom CSS for sidebar and wider content area
sidebar_width = 300  
content_width = "60%"  


# Custom CSS for layout
st.markdown(f"""
        <style>
     /* Set background image for the whole web app */

       .stApp {{

           background-image: url('https://t4.ftcdn.net/jpg/05/25/26/21/240_F_525262195_v4azGeY3sADY0rBet5iX7vmbgrEmwRv0.jpg');
           background-size: cover; /* Cover the entire area */       
           background-repeat: no-repeat; /* Prevent repeating the image */       
           background-position: center; /* Center the background image */

           background-opacity:0.4; /* Set the desired opacity */

        }}

        /* Increase the sidebar width */
        .css-1d391kg {{
            width: {sidebar_width}px;
        }}
        /* Increase the content area width */
        .css-1outpf8 {{
            width: {content_width};
            margin-left: {sidebar_width}px; /* Make space for the sidebar */
        }}
        /* Optional: Style sidebar header */
        .css-1fzr9py {{
            
            font-size: 20px;
            font-weight: bold;
        }}
        </style>
    """, unsafe_allow_html=True)


# Open AI key used for chat bot
openai.api_key = #your open ai key



# In-memory storage for users 
if "users" not in st.session_state:
    st.session_state.users = {"user1": "password123"}

     # Track login status
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = ""

# Functions for login, sign-up, and sending feedback
def login(username, password):
    # Check if the username exists
       if username not in st.session_state.users:
        st.warning("Username doesn't exist. Please sign up.")
       elif st.session_state.users[username] != password:
        # If the password is incorrect
        st.warning("Incorrect password. Please try again.")
       else:
        # If login is successful
        st.session_state.logged_in = True
        st.session_state.current_user = username
        st.success("Logged in successfully!")

def signup(username, password):
        if username in st.session_state.users:
         st.warning("Username already exists. Please choose a different username.")
        else:
         st.session_state.users[username] = password
         st.success("Account created successfully! You can now log in.")

def send_feedback(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    
     try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            email_body = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_body)
        st.success("Feedback sent successfully!")
     except Exception as e:
        st.error(f"Failed to send feedback: {e}")



# Function to generate GPT-3 responses
def get_gpt_response(query, context):
    prompt = f"""
    Below is the dataset:
    {context}

    Answer the question based on the dataset:
    {query}
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        # max_tokens=150,
        temperature=0.7
    )

    answer = response.choices[0].message.content.strip()

    return answer

 # Handles login/signup process and show dashboard only when logged in
if not st.session_state.logged_in:
    # Login and Signup page
    st.title("Welcome Login to Continue...")

    auth_option = st.selectbox("Choose an option", ["Login", "Sign Up"])

    if auth_option == "Login":
        st.header("Login Page")
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            login(username_input, password_input)

    elif auth_option == "Sign Up":
        st.header("Sign Up Page")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        signup_button = st.button("Sign Up")

        if signup_button:
           signup(new_username, new_password)

else:
    # Once logged in, show the dashboard
    st.sidebar.success(f"Welcome, {st.session_state.current_user}!")  

    # side bar for navigation panel
    st.sidebar.image(r"C:\Users\yashw\Desktop\infosys internship\logo.png", use_container_width=True)
    nav_buttons = ["Overview", "GDP Metrics", "Unemployment Metrics", "Sector Metrics", "R&D patents", "Feedback"   ]
    nav_button = st.sidebar.radio("Navigation", nav_buttons)
    # Logout button
    if st.sidebar.button("Logout"):
            # Reset session states
        st.session_state.logged_in = False
        st.session_state.current_user = ""
        st.sidebar.success("You have been logged out.")


    st.sidebar.markdown("""

    <hr>

    <div style='text-align: center;'>

         Created  by 
        Yashwanth Sai Kasarabada

       || --- All Rights Reserved --- ||

     </div>

    """, unsafe_allow_html=True)


   # navigation panel development through else if condition
   # overview section
    if nav_button == "Overview":
            # Chatbot section 
            st.subheader(" Chatbot Q/A of Data")
        
            user_input = st.text_input("Ask any question :")

        
            st.header("Overview of Power BI Report ")
            st.write("""
                     Gross Domestic Product (GDP) serves as a vital measure of economic health, representing the total value of goods and services produced within a specific region during a given period. It is a cornerstone metric for analyzing economic performance and regional development.
             
                     This dashboard delves into multiple facets of India's urban economic landscape, with a focus on:
             
                     1.GDP Metrics:
                     Explore the overall GDP contributions from various cities and regions in India, showcasing their economic strengths and growth patterns.
             
                     2.Unemployment Metrics:
                     Analyze unemployment trends to understand labor market dynamics and their correlation with economic performance across different regions.
             
                     3.Sector-Wise Metrics:
                     Dive into sectoral contributions to the economy, including key industries such as agriculture, information and communication technology (ICT), manufacturing, and services.
             
                     4.R&D and Patents:
                     Gain insights into innovation-driven growth by examining research and development (R&D) investments and patent statistics, highlighting the role of technological advancements in urban economies.
                    """) 
    
       
            # Power bi Dashboard
            dashboard_url = " https://app.fabric.microsoft.com/reportEmbed?reportId=3cefbaca-703b-42e9-87cd-85c241dce536&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b"
            st.markdown(f"""
        
              <iframe title="IndiacityGdp_infosys_project_yash"  width="1000" Height="600" src="https://app.fabric.microsoft.com/reportEmbed?reportId=3cefbaca-703b-42e9-87cd-85c241dce536&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b" frameborder="0" allowFullScreen="true"></iframe>
        
               """, unsafe_allow_html=True)
  
    # GDP section
    elif nav_button == "GDP Metrics":
        st.header("GDP and GDP Per Capita")
        fig = px.bar(df_Gdp, x='City', y='Average GDP (in billion $)', 
                    title="  Average Gdp of India's Tier 1 citites (2019-2024)", 
                    labels={'Average GDP (in billion $)': 'Average GDP (in billion $)'})
        st.plotly_chart(fig)
        fig = px.bar(df_Gdp_per_capita, x='City', y='Average GDP per Capita (in $)', 
                    title="  Average Gdp Per capita of India's Tier 1 citites (2019-2024)", 
                    labels={'Average GDP per Capita (in $)': 'Average GDP per Capita (in $)'})
        st.plotly_chart(fig)
        st.write("""
        GDP?\n
            Gross Domestic Product (GDP) is the monetary value of all goods and services produced within a country's borders over a specific period, typically a year. It serves as a measure of a country's economic performance and overall size of its economy.
            
            For cities, GDP highlights their economic contribution to the national economy, driven by industries, trade, services, and innovation.
            
        GDP Per Capita?\n
            GDP per capita is the average economic output per person. It is calculated by dividing the total GDP of a region by its population. This metric provides an estimate of the average income or economic productivity of an individual in a specific area.
            
            Formula:
            GDP per capita = GDP \ Population
            
             
            
        Difference Between GDP and GDP Per Capita\n
            GDP measures the total economic activity of a city or country and reflects its overall economic size and strength.
             
            GDP per capita provides a per-person perspective, highlighting the standard of living, wealth distribution, and individual productivity.
            For instance:
            
            Mumbai has the highest GDP (360 billion USD) but does not have the highest GDP per capita, as its large population reduces the per-person economic output.
            Delhi has the highest GDP per capita (5003.08 USD), indicating a higher average income or productivity per resident despite having a smaller total GDP compared to Mumbai.
            GDP and GDP Per Capita of Indian Cities
            Cities with the Highest and Lowest GDP:
            
            Highest GDP: Mumbai, the financial capital, averages 360 billion USD, driven by its financial markets, manufacturing, and global trade.
            Lowest GDP: Jaipur, a cultural city, averages 34.83 billion USD, reliant on tourism and traditional industries.
            Cities with the Highest and Lowest GDP Per Capita:
            
            Highest GDP Per Capita: Delhi, averaging 5003.08 USD, reflects high productivity and a significant services sector presence.
            Lowest GDP Per Capita: Jaipur, averaging 1950 USD, points to a lower income or productivity per individual.
            How Indian Cities Contribute to Overall GDP
            India's GDP (approximately $3.73 trillion as of 2024) is driven by urban centers:
            
        Top Contributors:
            
            Mumbai: Finance, manufacturing, and trade.
            Delhi: Government services and technology.
            Bangalore: IT and startups.
            Chennai: Automobile and port trade.
            Developing Cities:
            
            Ahmedabad and Hyderabad are emerging as industrial and IT hubs, respectively.
            Jaipur and Lucknow have potential growth areas but lag in absolute and per capita GDP.
        Key Insights and Trends \n
            Economic Powerhouses:
            Mumbai s GDP highlights its dominance, while Delhi  high GDP per capita showcases wealth and productivity.
            
            Wealth Disparity:
            The gap between Mumbai (highest GDP) and Jaipur (lowest GDP) underscores regional economic disparities. Addressing these differences can support more balanced growth.
            
            Growth Opportunities:
            Investments in Tier-2 cities can accelerate their GDP contributions and improve GDP per capita through infrastructure, technology, and skill development.
            
        """)
    
    # sector Metrics Section
    elif nav_button == "Sector Metrics":
        st.header("Sector Wise Metrics")
        st.write("""
            Productivity can be analyzed at the sectoral level to understand how efficiently different industries contribute to GDP. 
            Major sectors that influence productivity in India include:
            
            - **Agriculture**: Despite a large portion of the population being employed in agriculture, it contributes a smaller share to GDP.
            - **Manufacturing**: Key to India's industrial growth, including automotive, textiles, and heavy industries.
            - **ICT (Information and Communication Technology)**: The IT sector has experienced rapid growth, contributing significantly to GDP and employment.
            - **Services**: This sector, including finance, education, healthcare, and hospitality, is the largest contributor to India's GDP.
         """)
        # Sector selection
        sector = st.selectbox("Select a sector to view its productivity trends", ["Agriculture", "Industrial", "ICT", "Tourism"])

        # Show line chart of sectoral productivity
        fig = px.line(df_sector, x='Year', y=sector, title=f"{sector} Productivity Over Years", labels={'value': f'{sector} Productivity (%)'})
        st.plotly_chart(fig)

        # Additional insights based on selected sector
        if sector == "Agriculture":
            st.write("""
                Agriculture remains one of the largest employers in India, but its contribution to GDP has been declining 
                due to factors like urbanization, reduced arable land, and modern technology.
            """)
        elif sector == "Manufacturing":
            st.write("""
                Manufacturing plays a crucial role in driving industrial growth in India. Sectors such as automotive, textiles, and heavy machinery 
                continue to grow, though challenges like labor costs and automation are changing the landscape.
            """)
        elif sector == "ICT":
            st.write("""
                The ICT sector has experienced rapid growth, contributing significantly to India's GDP. The rise of digital technologies 
                and software services have made India a global hub for IT outsourcing.
            """)
        elif sector == "Tourism":
            st.write("""
                Tourism is a growing sector in India, with its contribution to the economy being driven by both domestic and international tourism. 
                The rise of travel and hospitality services has led to an increase in employment and economic activity in tourism-related regions.
            """)
        elif sector == "Employment":
            st.write("""
                Employment trends in India show variation across sectors. While the services and ICT sectors are seeing growth, 
                agriculture and manufacturing face challenges due to changing market dynamics and technology adoption.
            """)
            st.write("""
                Understanding sectoral productivity helps policymakers focus on areas of potential growth and improvement. 
                For example, the ICT sector's rise has been driven by increasing internet penetration and tech innovations, 
                while the decline in agriculture s share of GDP signals the need for innovation in farming practices.
        """)
            st.plotly_chart(fig)
        st.write("Sectoral Contribution to GDP (by Year):")
        fig2 = px.bar(df_sector, x='Year', y=['Agriculture', 'Industrial', 'ICT', 'Tourism', 'Services'], barmode='group', title="Sectoral Contribution to GDP and Employment")
        st.plotly_chart(fig2)

    # Unemployment Metrics Section
    elif nav_button == "Unemployment Metrics":
        st.header(" Unemployment Metrics ")
       # bar chart for employment rate
        fig = px.bar(df_Unemployment, x='Year', y='Unemployment Rate', 
                    title="Year-wise  Average Unemployment Rate (2019-2024)", 
                    labels={'Unemployment Rate': 'Unemployment Rate (%)'})
        st.plotly_chart(fig)

        st.write("""
            Regularly track shifts in sectoral contributions and unemployment rates to fine-tune policy responses.\n
            Avg Unemployment Rates -(City Wise)
         
                    Ahmedabad: 7.8%  

                    Bangalore: 6.2% 

                    Chennai: 8.4%

                    Delhi: 10.9%

                    Hyderabad: 9.1%

                    Kolkata: 7.2%

                    Mumbai: 11.5%

                    Pune: 6.8%     

            Overall Unemployment Trends:

            The general unemployment rate across all demographics shows year-to-year fluctuations. The lowest average rate was recorded in 2021 (5.28%), while the highest was in 2019 (6.66%). This indicates some economic recovery or effective job market interventions post-2019.
           
            Youth Unemployment:
            
            The youth unemployment rate remains consistently higher than the overall rate. This trend highlights structural challenges in integrating young workers into the job market, possibly due to skill mismatches, lack of entry-level opportunities, or economic downturns affecting new job creation.
            Sectoral Employment Analysis

            Tourism Sector Employment:
            
            The tourism sector contributes directly to reducing unemployment by creating jobs in travel, hospitality, and related industries.
            A higher proportion of employment in this sector correlates with lower unemployment rates, underlining its importance in job creation, especially in urban centers.
            
            ICT Sector Employment:
            
            The ICT sector has a notable impact on reducing unemployment. It creates high-quality, skill-based jobs and contributes to urban and semi-urban economic growth.
            Years with higher ICT sector contributions (e.g., 2022) saw more stable unemployment rates, emphasizing its potential as a driver for economic resilience.
            
            SME Employment:
            
            Small and Medium Enterprises are critical for grassroots employment. Declines in SME employment percentages (e.g., 2020) might have contributed to spikes in unemployment during those years.
            Economic Indicators and Unemployment
            GDP and GDP Per Capita:
            
            An inverse correlation is observed between GDP growth and unemployment rates. Higher GDP per capita, representing better economic health, aligns with lower unemployment levels.
            In 2021, a significant GDP improvement coincided with the lowest unemployment rate, indicating the effectiveness of economic policies or recovery efforts.
            Sectoral Contributions to GDP:
            
            Shifts in sectoral contributions (e.g., agriculture, industry, services) influence unemployment:
            Years with declining industrial or service sector percentages showed an uptick in unemployment rates, indicating their critical role in providing jobs.
            Correlations and Observations
            Youth Unemployment vs. ICT Sector:
            
            An increase in ICT sector employment correlates with a reduction in youth unemployment. This suggests ICT-related education and training programs could have a transformative impact.
            Tourism Sector and GDP:
            
            Regions or years with higher tourism sector contributions report reduced unemployment, showing the sector’s potential in diversifying the job market.
            
            SME Employment:
            
            As SMEs often serve as the backbone of local economies, a higher SME employment percentage correlates with reduced overall and youth unemployment rates.
            Challenges Identified
            Youth Unemployment: The persistent gap between youth and overall unemployment highlights the need for targeted policies.
            Sectoral Variability: A heavy reliance on specific sectors (e.g., ICT, tourism) leaves regions vulnerable to sectoral downturns.
            Economic Inequality: Regions or years with lower GDP per capita struggle with higher unemployment, reflecting disparities in economic distribution.
            Recommendations
           
            Policy Focus on Youth Employment:
            
            Invest in vocational training, internships, and skill development programs to address youth unemployment.
            Promote entrepreneurship among young people, especially in SME sectors.
            
            Diversify Employment Opportunities:
            
            Reduce over-reliance on a few sectors by developing other high-potential industries.
            Strengthen tourism infrastructure to boost employment in underperforming regions.
            
            Support SMEs and ICT Growth:
            
            Provide financial incentives and subsidies to SMEs for hiring and expansion.
            Invest in ICT training programs to align the workforce with market demands.
            
            Monitor Sectoral Contributions:
            
               

            
        """)
   
     # R & D , Patents Section 
    elif nav_button == "R&D patents":
        st.header("Research and Development , Patents per 1000 Inhibitants section ")   

  

      # Select box to choose a city
        city = st.selectbox("Select a city to view its average values", list(city_data.keys()))

       # Show average values for the selected city
        if city in city_data:
           selected_data = city_data[city]
           st.write(f"**Average GDP (in billion $)**: {selected_data['GDP']}")
           st.write(f"**Average GDP per capita (in $)**: {selected_data['GDP per capita']}")
           st.write(f"**Average R&D Expenditure (% of GDP)**: {selected_data['R&D Expenditure']}")
           st.write(f"**Average Patents per 100,000 Inhabitants**: {selected_data['Patents']}")    
           st.write("Avg R & D And Patents to GDP :")
        fig2 = px.bar(df_Rdpatents, x='City', y=['Average R&D Expenditure (% of GDP)','Average Patents per 100,000 Inhabitants'], barmode='group', title="Avgerage R&D Expenditure and patents per 1000 inhabitants ")
        st.plotly_chart(fig2)
           
          
              
       
        st.write("""
            R&D Expenditure (% of GDP):
             
            Peak: 2020 (1.93%), likely due to COVID-driven innovation.
            Low: 2023 (0.73%), reflecting reduced innovation focus.
            Higher R&D spending correlates with technological advancements and economic growth.
            
            Patents per 100,000 Inhabitants:
             
            Peak: 2021 (6.6 patents), following significant R&D investment.
            Low: 2023 (2.9 patents), aligning with minimal R&D funding.
            High patent activity is linked to stronger ICT and industrial sectors.
            
            Key Insights:

            Correlation: Strong link between R&D spending and patent filings.
            Economic Impact: Boosts high-tech employment and GDP growth.
            Challenges: Volatile R&D investments and underutilized patents hinder potential.
            
            Recommendations:
             
            Sustain consistent R&D funding.
            Promote innovation in underperforming regions.
            Facilitate commercialization of patents through incubation programs.
            Regularly evaluate R&D and patent impact on the economy.
             """)
      
       # Feeback section
    elif nav_button == "Feedback":
        st.header("Feedback Form")
        st.write("""
            We value your feedback! Please let us know your thoughts on the dashboard, its content, and any improvements you'd like to see.""")

        subject = st.text_input("Subject")
        message = st.text_area("Message")
        if st.button("Submit Feedback"):
            smtp_server = "SERVER_MAIL_ID"
            smtp_port = "PORT_NO"
            smtp_user = "USER_ID"
            smtp_pass = "YOUR_SMTP_PASS"
            sender_email = "your_sender_email"
            receiver_email = "your_receiver_email"

            if not subject or not message:
                st.warning("Please fill in both subject and message.")
            else:
                send_feedback(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_user, smtp_pass)

    
