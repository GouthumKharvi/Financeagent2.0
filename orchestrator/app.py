                                                                           #working
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import shutil

# Initialize FastAPI app
app = FastAPI()

# Allow CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Original dummy_qa dictionary (unchanged keys)
dummy_qa = {
    "What is a stock?": "A stock represents ownership in a company and a claim on part of its assets and earnings.",
    "What is a bond?": "A bond is a fixed-income instrument that represents a loan made by an investor to a borrower.",
    "What is mutual fund?": "A mutual fund is an investment vehicle made up of a pool of money collected from many investors to invest in securities.",
    "What is ETF?": "An ETF, or exchange-traded fund, is a type of investment fund traded on stock exchanges.",
    "What is a dividend?": "A dividend is a distribution of a portion of a company's earnings to its shareholders.",
    "What is the difference between stocks and bonds?": "Stocks represent ownership; bonds are loans to companies/governments.",
    "What is a portfolio?": "A portfolio is a collection of financial investments like stocks, bonds, and cash equivalents.",
    "What is diversification in finance?": "Diversification is a risk management strategy that mixes a wide variety of investments within a portfolio.",
    "What is an index fund?": "An index fund is a mutual fund or ETF designed to track a specified basket of underlying investments.",
    "What is compound interest?": "Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest.",
    "What is inflation?": "Inflation is the rate at which the general level of prices for goods and services is rising.",
    "What is deflation?": "Deflation is a decrease in the general price level of goods and services.",
    "What is GDP?": "Gross Domestic Product (GDP) is the total monetary value of all finished goods and services produced within a country's borders.",
    "What is a recession?": "A recession is a period of temporary economic decline during which trade and industrial activity are reduced.",
    "What is a bear market?": "A bear market is a market condition where prices of securities are falling, and widespread pessimism causes a negative sentiment.",
    "What is a bull market?": "A bull market is a financial market in which prices are rising or expected to rise.",
    "What is financial planning?": "Financial planning is the process of estimating the capital required and determining its competition.",
    "What is retirement planning?": "Retirement planning is the process of determining retirement income goals and the actions necessary to achieve them.",
    "What is an emergency fund?": "An emergency fund is money set aside to cover unexpected expenses.",
    "What is credit score?": "A credit score is a number between 300–850 that depicts a consumer's creditworthiness.",
    "What is budgeting?": "Budgeting is creating a plan to spend your money wisely.",
    "What is net worth?": "Net worth is the value of all assets, minus the total of all liabilities.",
    "What is a savings account?": "A savings account is a deposit account held at a financial institution that provides principal security and a modest interest rate.",
    "What is a checking account?": "A checking account is a deposit account held at a bank that allows withdrawals and deposits.",
    "What is liquidity?": "Liquidity refers to how easily an asset can be converted into cash.",
    "What is ROI?": "Return on Investment (ROI) is a measure used to evaluate the efficiency of an investment.",
    "What is APR?": "APR stands for Annual Percentage Rate and represents the yearly interest rate charged on borrowed money.",
    "What is credit utilization ratio?": "Credit utilization ratio is the amount of credit used compared to the total credit available.",
    "What is a 401(k)?": "A 401(k) is a retirement savings plan offered by many American employers that has tax advantages for the saver.",
    "What is an IRA?": "An IRA is an Individual Retirement Account that allows individuals to direct pre-tax income toward investments.",
    "What is financial literacy?": "Financial literacy is the ability to understand and effectively use various financial skills.",
    "What is passive income?": "Passive income is earnings derived from a rental property, limited partnership, or other enterprises in which a person is not actively involved.",
    "What is an asset?": "An asset is any resource owned by an individual or entity that is expected to provide future economic benefits.",
    "What is a liability?": "A liability is something a person or company owes, usually a sum of money.",
    "What is a capital gain?": "A capital gain is an increase in the value of a capital asset that gives it a higher worth than the purchase price.",
    "What is a financial advisor?": "A financial advisor is a professional who provides financial guidance and advice to clients.",
    "What is a stockbroker?": "A stockbroker is a regulated professional who buys and sells stocks on behalf of clients.",
    "What is technical analysis?": "Technical analysis is the study of price and volume charts to predict future market movements.",
    "What is fundamental analysis?": "Fundamental analysis evaluates a security by examining related economic and financial factors.",
    "What is a margin account?": "A margin account allows a broker to lend money to an investor to buy securities.",
    "What is a market order?": "A market order is an order to buy or sell a stock immediately at the best available price.",
    "What is a limit order?": "A limit order is an order to buy or sell a stock at a specific price or better.",
    "What is a stop-loss order?": "A stop-loss order is designed to limit an investor's loss on a position.",
    "What is the Federal Reserve?": "The Federal Reserve is the central banking system of the United States.",
    "What is monetary policy?": "Monetary policy involves the management of money supply and interest rates by central banks.",
    "What is fiscal policy?": "Fiscal policy is the use of government spending and tax policies to influence economic conditions.",
    "What is quantitative easing?": "Quantitative easing is a monetary policy where a central bank buys government bonds to inject money into the economy.",
    "What is a credit card APR?": "Credit card APR is the annual rate charged for borrowing through a credit card.",
    "What is FICO score?": "FICO score is a type of credit score created by the Fair Isaac Corporation.",
    "What is bankruptcy?": "Bankruptcy is a legal process where a person or entity declares inability to repay debts.",
    "How does mutual fund work?": "Mutual fund works by accruing interest.",
    "Should I invest in real estate?": "Investing in real estate can be beneficial if you want regular income.",
    "How does online banking work?": "Online banking allows users to manage accounts via the internet.",

    # Voice command responses
    "Check my portfolio": "Sure, your current portfolio includes 50% stocks, 30% bonds, and 20% mutual funds.",
    "Show me my investment summary": "Here's your investment summary: Total value is $100,000, with 8% annual growth.",
    "What is my net worth?": "Your current estimated net worth is $150,000.",
    "Transfer $500 to savings": "Transferring $500 to your savings account now.",
    "What's the status of my loan?": "Your loan is active with a balance of $15,000 and 5% interest rate.",
    "What is my credit score?": "Your current credit score is 750, which is considered good.",
    "Pay my credit card bill": "Your credit card bill of $300 has been scheduled for payment.",
    "How much did I spend last month?": "You spent $2,400 last month across all accounts.",
    "Set a budget for groceries": "Budget for groceries has been set to $300 per month.",
    "Remind me to invest in mutual funds": "Reminder set to invest in mutual funds tomorrow.",
    "Alert me if stock price drops": "Alert will be sent if the specified stock drops below your set threshold.",
    "Show me latest finance news": "Here are the top finance news headlines for today.",
    "Summarize my spending": "You spent 40% on essentials, 30% on savings, and 30% on discretionary items.",
    "Open my investment dashboard": "Opening your investment dashboard now.",
    "What are my top-performing assets?": "Your top-performing assets are Apple, Microsoft, and Tesla.",
    "Suggest me a saving plan": "I suggest a 50/30/20 plan: 50% needs, 30% wants, 20% savings.",
    "Track my stock performance": "Tracking your stock portfolio. Overall gain this week: 5%.",
    "Is it a good time to invest?": "Based on market trends, this could be a reasonable time to invest cautiously.",
    "Tell me about my expenses": "Your major expenses this month include rent, groceries, and utilities.",
    "How much can I invest safely?": "You can safely invest around $1,000 based on your current expenses.",
    "How is the market today?": "Markets are up today. The S&P 500 gained 1.2%, Nasdaq up 0.9%.",
    "Show me my recent transactions": "Here are your last 5 transactions including purchases and transfers.",
    "Add money to my emergency fund": "Adding $200 to your emergency fund.",
    "Analyze my budget": "You are under budget this month by $150.",
    "What’s my retirement status?": "You have saved 30% of your retirement goal.",
    "Forecast my finances": "Based on current trends, your savings will reach $50,000 in 3 years.",
    "Open stock chart for Apple": "Opening live stock chart for Apple Inc.",
    "What is the interest on my savings account?": "Your savings account earns 4% annual interest.",
    "Pay my rent": "Rent payment of $1,200 has been scheduled.",
    "Show my financial goals": "You have 3 goals: Save for house, emergency fund, and retirement.",
    "What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?": "Today, your Asia tech allocation is 22 % of AUM, up from 18 % yesterday. TSMC beat estimates by 4 %, Samsung missed by 2 %. Regional sentiment is neutral with a cautionary tilt due to rising yields."

}

# Create a normalized version of dummy_qa with lowercase keys for case-insensitive matching
normalized_qa = {k.lower().strip(): v for k, v in dummy_qa.items()}

@app.post("/query-text/")
async def query_text(user_input: str = Form(...)):
    normalized_input = user_input.lower().strip()
    answer = normalized_qa.get(normalized_input, "I'm sorry, I don't have an answer for that question.")
    return JSONResponse(content={"response": answer, "fallback": False})


@app.post("/query-voice/")
async def query_voice(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(file.file, tmp)
        temp_audio_path = tmp.name

    # Simulated transcription (you can replace with real transcription)
    transcribed_text = "Today, your Asia tech allocation is 22 % of AUM, up from 18 % yesterday. TSMC beat estimates by 4 %, Samsung missed by 2 %. Regional sentiment is neutral with a cautionary tilt due to rising yields."
    

    normalized_text = transcribed_text.lower().strip()
    answer = normalized_qa.get(normalized_text, "I'm sorry, I don't have an answer for that question.")
    return JSONResponse(content={"response": answer, "fallback": False})
