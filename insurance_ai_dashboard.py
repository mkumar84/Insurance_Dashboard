# insurance_ai_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import plotly.express as px
import time

# Set page config
st.set_page_config(
    page_title="InsureAI Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Generate fake data functions
def generate_policies(num=50):
    products = ["Home", "Auto", "Life", "Health", "Travel"]
    statuses = ["Active", "Expired", "Pending", "Cancelled"]
    start_date = datetime.now() - timedelta(days=365*3)
    
    data = []
    for i in range(num):
        start = start_date + timedelta(days=random.randint(0, 365*3))
        end = start + timedelta(days=365)
        premium = round(random.uniform(100, 2000), 2)
        data.append({
            "Policy ID": f"POL{10000 + i}",
            "Product": random.choice(products),
            "Holder": f"Customer {i+1}",
            "Start Date": start.strftime("%Y-%m-%d"),
            "End Date": end.strftime("%Y-%m-%d"),
            "Premium": premium,
            "Status": random.choice(statuses),
            "Agent": f"Agent {random.randint(1, 10)}"
        })
    return pd.DataFrame(data)

def generate_claims(num=30):
    types = ["Auto Collision", "Property Damage", "Medical", "Theft", "Natural Disaster"]
    statuses = ["Submitted", "In Review", "Approved", "Denied", "Paid"]
    
    data = []
    for i in range(num):
        claim_date = datetime.now() - timedelta(days=random.randint(0, 180))
        amount = round(random.uniform(500, 50000), 2)
        data.append({
            "Claim ID": f"CLM{20000 + i}",
            "Policy ID": f"POL{10000 + random.randint(0, 49)}",
            "Type": random.choice(types),
            "Date Filed": claim_date.strftime("%Y-%m-%d"),
            "Amount": amount,
            "Status": random.choice(statuses),
            "Customer": f"Customer {random.randint(1, 50)}",
            "AI Flag": random.choice(["Low Risk", "Medium Risk", "High Risk"])
        })
    return pd.DataFrame(data)

def generate_underwriting_cases(num=20):
    risks = ["Low", "Medium", "High", "Very High"]
    statuses = ["New", "In Review", "Approved", "Declined"]
    
    data = []
    for i in range(num):
        data.append({
            "Case ID": f"UW{30000 + i}",
            "Applicant": f"Applicant {i+1}",
            "Product": random.choice(["Home", "Life", "Health"]),
            "Risk Assessment": random.choice(risks),
            "AI Recommendation": random.choice(["Approve", "Approve with Conditions", "Decline", "Further Review"]),
            "Status": random.choice(statuses),
            "Date": (datetime.now() - timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d")
        })
    return pd.DataFrame(data)

def generate_marketing_opportunities(num=15):
    channels = ["Email", "Direct Mail", "Social Media", "Web", "Partner"]
    stages = ["Lead", "Contacted", "Proposal", "Negotiation", "Closed-Won", "Closed-Lost"]
    
    data = []
    for i in range(num):
        data.append({
            "Opportunity ID": f"OPP{40000 + i}",
            "Customer": f"Prospect {i+1}",
            "Product Interest": random.choice(["Auto", "Home", "Life", "Bundle"]),
            "Channel": random.choice(channels),
            "Stage": random.choice(stages),
            "Potential Premium": round(random.uniform(500, 5000), 2),
            "AI Score": round(random.uniform(0, 1), 2)
        })
    return pd.DataFrame(data)

def generate_sales_data(num=100):
    products = ["Auto", "Home", "Life", "Health", "Travel"]
    agents = [f"Agent {i}" for i in range(1, 11)]
    regions = ["North", "South", "East", "West", "Central"]
    
    data = []
    for i in range(num):
        date = datetime.now() - timedelta(days=random.randint(0, 365))
        data.append({
            "Sale ID": f"SAL{50000 + i}",
            "Date": date.strftime("%Y-%m-%d"),
            "Product": random.choice(products),
            "Agent": random.choice(agents),
            "Region": random.choice(regions),
            "Premium": round(random.uniform(200, 3000), 2),
            "Commission": round(random.uniform(20, 300), 2)
        })
    return pd.DataFrame(data)

def generate_eapp_data(num=10):
    statuses = ["Started", "In Progress", "Submitted", "Under Review", "Approved", "Declined"]
    
    data = []
    for i in range(num):
        start = datetime.now() - timedelta(days=random.randint(0, 30))
        data.append({
            "Application ID": f"EAPP{60000 + i}",
            "Customer": f"Applicant {i+1}",
            "Product": random.choice(["Auto", "Home", "Life"]),
            "Start Time": start.strftime("%Y-%m-%d %H:%M"),
            "Last Activity": (start + timedelta(minutes=random.randint(5, 120))).strftime("%Y-%m-%d %H:%M"),
            "Status": random.choice(statuses),
            "AI Assistance Used": random.choice([True, False]),
            "Completion %": random.randint(10, 100)
        })
    return pd.DataFrame(data)

# Generate all data
policies_df = generate_policies()
claims_df = generate_claims()
underwriting_df = generate_underwriting_cases()
marketing_df = generate_marketing_opportunities()
sales_df = generate_sales_data()
eapp_df = generate_eapp_data()

# Mock AI functions for demo purposes
def mock_claim_summarization(claim_id):
    time.sleep(1)  # Simulate processing
    summaries = {
        "description": f"The claimant reported a {random.choice(['minor', 'moderate', 'major'])} "
                      f"{random.choice(['collision', 'weather-related', 'theft', 'fire'])} incident. "
                      "The claimant states the incident occurred at "
                      f"{random.choice(['home', 'a parking lot', 'on the highway'])}.",
        "key_factors": [
            f"{random.choice(['Police', 'Witness'])} report available",
            f"{random.choice(['Photos', 'Videos'])} submitted",
            f"{random.choice(['Previous claims', 'No prior claims'])} found"
        ],
        "ai_assessment": random.choice(["Likely valid", "Potentially fraudulent", "Needs further investigation"]),
        "recommended_action": random.choice(["Approve claim", "Request additional documentation", "Investigate further"])
    }
    return summaries

def mock_underwriting_recommendation(case_id):
    time.sleep(0.5)
    return {
        "risk_factors": [
            f"{random.choice(['Age', 'Occupation', 'Medical history'])}: {random.choice(['Low risk', 'Medium risk', 'High risk'])}",
            f"{random.choice(['Location', 'Property type', 'Driving record'])}: {random.choice(['Favorable', 'Average', 'Unfavorable'])}"
        ],
        "ai_score": round(random.uniform(0, 1), 2),
        "recommendation": random.choice(["Approve as standard", "Approve with premium adjustment", "Decline", "Refer to senior underwriter"])
    }

def mock_eapp_assistance():
    return {
        "suggested_fields": random.sample([
            "Medical history details",
            "Vehicle information",
            "Property details",
            "Beneficiary information",
            "Driver details"
        ], k=2),
        "completion_tips": [
            "Consider adding additional driver information",
            "Review medical history section for completeness"
        ],
        "estimated_time_saved": f"{random.randint(5, 25)} minutes"
    }

# Sidebar navigation
st.sidebar.image("https://via.placeholder.com/150x50?text=InsureAI", width=150)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Dashboard Overview", 
    "Claims Automation", 
    "Claims Summarization",
    "Underwriting AI",
    "Marketing & Sales",
    "eApplications"
])

# Helper function for metrics cards
def create_metric_card(label, value, delta=None, help_text=None):
    col = st.columns(1)[0]
    col.metric(label=label, value=value, delta=delta, help=help_text)

# Main content area
if page == "Dashboard Overview":
    st.title("InsureAI - Insurance Platform Dashboard")
    st.write("AI-powered solutions for modern insurance operations")
    
    # KPI Row
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_metric_card("Active Policies", "1,248", "+5.2% vs last month")
    with col2:
        create_metric_card("Claims This Month", "87", "-2.3% vs last month")
    with col3:
        create_metric_card("Underwriting AI Adoption", "73%", "+12% vs last quarter")
    with col4:
        create_metric_card("eApp Completion Rate", "68%", "+8% vs last month")
    
    # Charts Row
    st.subheader("Performance Trends")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Sales by product
        sales_by_product = sales_df.groupby("Product")["Premium"].sum().reset_index()
        fig = px.bar(sales_by_product, x="Product", y="Premium", title="Premium by Product")
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # Claims status
        claims_by_status = claims_df.groupby("Status")["Claim ID"].count().reset_index()
        fig = px.pie(claims_by_status, values="Claim ID", names="Status", title="Claims by Status")
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent activity
    st.subheader("Recent Activity")
    activity_col1, activity_col2 = st.columns(2)
    
    with activity_col1:
        st.write("**Recent Claims**")
        st.dataframe(claims_df.sort_values("Date Filed", ascending=False).head(5), hide_index=True)
    
    with activity_col2:
        st.write("**Underwriting Cases**")
        st.dataframe(underwriting_df.sort_values("Date", ascending=False).head(5), hide_index=True)

elif page == "Claims Automation":
    st.title("Claims Automation Center")
    st.write("AI-powered claims processing and fraud detection")
    
    tab1, tab2, tab3 = st.tabs(["Claims Queue", "Fraud Detection", "Automation Stats"])
    
    with tab1:
        st.subheader("Claims Processing Queue")
        st.dataframe(claims_df, use_container_width=True, hide_index=True)
        
        selected_claim = st.selectbox("Select a claim to process", claims_df["Claim ID"])
        if st.button("Process with AI"):
            with st.spinner("AI is processing the claim..."):
                # Simulate AI processing
                time.sleep(2)
                st.success("Processing complete!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("AI Recommendations")
                    st.write(f"Claim ID: {selected_claim}")
                    st.write("**Assessment:** Likely valid")
                    st.write("**Recommended Action:** Approve with standard review")
                    st.write("**Confidence Score:** 87%")
                
                with col2:
                    st.subheader("Next Steps")
                    st.write("1. Verify supporting documents")
                    st.write("2. Confirm policy coverage")
                    st.write("3. Process payment if approved")
                    
                    if st.button("Approve Claim", type="primary"):
                        st.success("Claim approved successfully!")
    
    with tab2:
        st.subheader("Potential Fraud Indicators")
        high_risk_claims = claims_df[claims_df["AI Flag"] == "High Risk"]
        
        if not high_risk_claims.empty:
            for _, claim in high_risk_claims.iterrows():
                with st.expander(f"Claim {claim['Claim ID']} - {claim['Type']}"):
                    st.write(f"**Policy:** {claim['Policy ID']}")
                    st.write(f"**Amount:** ${claim['Amount']:,.2f}")
                    st.write(f"**Risk Factors:**")
                    st.write("- Multiple claims in short period")
                    st.write("- Inconsistent incident description")
                    st.write("- Unusual payment request method")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"Investigate {claim['Claim ID']}"):
                            st.warning(f"Claim {claim['Claim ID']} flagged for investigation")
                    with col2:
                        if st.button(f"Clear {claim['Claim ID']}"):
                            st.success(f"Claim {claim['Claim ID']} cleared for processing")
        else:
            st.success("No high-risk claims detected")
    
    with tab3:
        st.subheader("Automation Performance")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Claims Processed Automatically", "342", "15% increase")
        with col2:
            st.metric("Average Processing Time", "2.1 hours", "45% reduction")
        with col3:
            st.metric("Fraud Detection Rate", "92%", "8% improvement")
        
        st.write("")
        st.write("**Automation Impact**")
        st.line_chart(pd.DataFrame({
            "Manual Processing": [100, 85, 70, 55, 40],
            "AI Processing": [0, 15, 30, 45, 60]
        }))

elif page == "Claims Summarization":
    st.title("Claims Document Summarization")
    st.write("AI-powered summarization of complex claim documents")
    
    selected_claim = st.selectbox("Select a claim to summarize", claims_df["Claim ID"])
    
    if st.button("Generate Summary"):
        with st.spinner("AI is analyzing claim documents..."):
            summary = mock_claim_summarization(selected_claim)
            time.sleep(2)
            
            st.subheader(f"Claim Summary for {selected_claim}")
            st.write(summary["description"])
            
            st.subheader("Key Factors")
            for factor in summary["key_factors"]:
                st.write(f"- {factor}")
            
            st.subheader("AI Assessment")
            cols = st.columns(3)
            cols[0].write(f"**Assessment:** {summary['ai_assessment']}")
            cols[1].write(f"**Confidence:** {random.randint(75, 95)}%")
            cols[2].write(f"**Recommendation:** {summary['recommended_action']}")
            
            st.divider()
            st.subheader("Supporting Documents")
            
            doc_types = ["Police Report", "Medical Records", "Repair Estimates", "Photos", "Witness Statements"]
            for doc in random.sample(doc_types, k=3):
                with st.expander(doc):
                    st.write(f"This is a simulated {doc.lower()} for claim {selected_claim}.")
                    st.write("**AI-extracted key points:**")
                    st.write(f"- {random.choice(['Document appears valid', 'No inconsistencies found', 'Potential issue detected'])}")
                    st.write(f"- {random.choice(['Dates match claim timeline', 'Signature present', 'Professional letterhead'])}")
            
            st.download_button("Download Full Summary", 
                             data=f"Simulated summary report for claim {selected_claim}",
                             file_name=f"summary_{selected_claim}.txt")

elif page == "Underwriting AI":
    st.title("AI Underwriting Assistant")
    st.write("Risk assessment and decision support for underwriters")
    
    tab1, tab2 = st.tabs(["Case Queue", "AI Recommendations"])
    
    with tab1:
        st.subheader("Underwriting Cases")
        st.dataframe(underwriting_df, use_container_width=True, hide_index=True)
    
    with tab2:
        selected_case = st.selectbox("Select a case for AI analysis", underwriting_df["Case ID"])
        
        if st.button("Generate AI Recommendation"):
            with st.spinner("AI is analyzing the underwriting case..."):
                recommendation = mock_underwriting_recommendation(selected_case)
                time.sleep(1.5)
                
                st.subheader(f"AI Underwriting Recommendation for {selected_case}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Risk Factors**")
                    for factor in recommendation["risk_factors"]:
                        st.write(f"- {factor}")
                    
                    st.write("")
                    st.write("**Supporting Data**")
                    st.write("- Credit score: Good")
                    st.write("- Loss history: Clean")
                
                with col2:
                    st.metric("AI Risk Score", recommendation["ai_score"])
                    st.write("**Recommendation:**")
                    st.success(recommendation["recommendation"])
                    
                    st.write("")
                    st.write("**Similar Historical Cases**")
                    st.write("- Case #UW24567: Approved with 10% premium increase")
                    st.write("- Case #UW19823: Approved as standard")
                
                st.divider()
                st.subheader("Next Steps")
                st.write("1. Review AI recommendation")
                st.write("2. Verify applicant information")
                st.write("3. Make final underwriting decision")
                
                decision = st.radio("Underwriting Decision", 
                                  ["Approve", "Approve with Conditions", "Decline", "Request More Info"])
                if st.button("Submit Decision"):
                    st.success(f"Decision submitted: {decision} for case {selected_case}")

elif page == "Marketing & Sales":
    st.title("Marketing & Sales Intelligence")
    st.write("AI-powered lead scoring and sales optimization")
    
    tab1, tab2, tab3 = st.tabs(["Opportunities", "Sales Performance", "AI Lead Scoring"])
    
    with tab1:
        st.subheader("Marketing Opportunities")
        st.dataframe(marketing_df.sort_values("AI Score", ascending=False), use_container_width=True, hide_index=True)
        
        st.subheader("Opportunity Distribution")
        fig = px.bar(marketing_df, x="Stage", y="Potential Premium", color="Product Interest",
                     title="Opportunities by Stage and Product")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Sales Performance")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Sales by Product**")
            product_sales = sales_df.groupby("Product")["Premium"].sum().reset_index()
            st.bar_chart(product_sales, x="Product", y="Premium")
        
        with col2:
            st.write("**Sales by Agent**")
            agent_sales = sales_df.groupby("Agent")["Premium"].sum().reset_index()
            st.bar_chart(agent_sales, x="Agent", y="Premium")
        
        st.write("")
        st.subheader("Recent Sales")
        st.dataframe(sales_df.sort_values("Date", ascending=False).head(10), use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("AI Lead Scoring")
        
        selected_opp = st.selectbox("Select opportunity for AI analysis", marketing_df["Opportunity ID"])
        opportunity = marketing_df[marketing_df["Opportunity ID"] == selected_opp].iloc[0]
        
        st.write(f"**Opportunity:** {selected_opp}")
        st.write(f"**Customer:** {opportunity['Customer']}")
        st.write(f"**Product Interest:** {opportunity['Product Interest']}")
        
        st.write("")
        st.subheader("AI Scoring Factors")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Positive Factors**")
            st.write("- Matches ideal customer profile")
            st.write("- Previous engagement with marketing")
            st.write("- High income bracket")
        
        with col2:
            st.write("**Negative Factors**")
            st.write("- No prior relationship")
            st.write("- Competitive quotes obtained")
            st.write("- Long sales cycle expected")
        
        st.write("")
        st.metric("AI Conversion Probability", f"{opportunity['AI Score']*100:.0f}%")
        
        st.progress(opportunity["AI Score"])
        
        st.write("")
        st.subheader("Recommended Actions")
        st.write("1. Personalize outreach with bundle options")
        st.write("2. Offer free consultation")
        st.write("3. Follow up within 3 days")

elif page == "eApplications":
    st.title("AI-Powered eApplications")
    st.write("Smart application assistance and completion analytics")
    
    tab1, tab2, tab3 = st.tabs(["Application Queue", "AI Assistance", "Completion Analytics"])
    
    with tab1:
        st.subheader("Current Applications")
        st.dataframe(eapp_df, use_container_width=True, hide_index=True)
        
        selected_app = st.selectbox("Select an application to review", eapp_df["Application ID"])
        application = eapp_df[eapp_df["Application ID"] == selected_app].iloc[0]
        
        st.write(f"**Application:** {selected_app}")
        st.write(f"**Customer:** {application['Customer']}")
        st.write(f"**Product:** {application['Product']}")
        st.write(f"**Status:** {application['Status']}")
        st.write(f"**Completion:** {application['Completion %']}%")
        
        st.progress(application["Completion %"] / 100)
    
    with tab2:
        st.subheader("AI Application Assistant")
        
        if st.button("Get AI Assistance"):
            with st.spinner("AI is analyzing the application..."):
                assistance = mock_eapp_assistance()
                time.sleep(1)
                
                st.success("AI suggestions ready!")
                st.write("**Suggested Fields to Complete:**")
                for field in assistance["suggested_fields"]:
                    st.write(f"- {field}")
                
                st.write("")
                st.write("**Completion Tips:**")
                for tip in assistance["completion_tips"]:
                    st.write(f"- {tip}")
                
                st.write("")
                st.write(f"**Estimated Time Saved:** {assistance['estimated_time_saved']}")
                
                st.download_button("Download Application Checklist", 
                                 data="Simulated application checklist",
                                 file_name="application_checklist.txt")
    
    with tab3:
        st.subheader("Application Analytics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Completion Rates by Product**")
            completion_by_product = eapp_df.groupby("Product")["Completion %"].mean().reset_index()
            st.bar_chart(completion_by_product, x="Product", y="Completion %")
        
        with col2:
            st.write("**AI Assistance Impact**")
            ai_impact = pd.DataFrame({
                "With AI": [65, 72, 80],
                "Without AI": [45, 50, 55]
            }, index=["Start Rate", "Completion Rate", "Approval Rate"])
            st.bar_chart(ai_impact)
        
        st.write("")
        st.subheader("Abandonment Analysis")
        st.write("**Top Abandonment Points:**")
        st.write("- Medical history section (32%)")
        st.write("- Beneficiary details (28%)")
        st.write("- Payment information (18%)")

# Add some styling
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4a8af4;
        color: white;
    }
    .stProgress > div > div > div {
        background-color: #4a8af4;
    }
</style>
""", unsafe_allow_html=True)