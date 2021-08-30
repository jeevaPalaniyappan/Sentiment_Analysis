from textblob import TextBlob

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "\" ['General Motors Recalls Newer Chevrolet Bolt EVs to Address Battery-Fire Risks', 'General Motors (GM) Misses Estimates on Chip Dearth, Lifts Full-Year Outlook', 'General Motors to replace battery modules for some Bolt electric vehicles after fire risks', 'General Motors to replace Chevrolet Camaro with an electric sedan: Report', \"\"Mediocre Returns on Capital At General Motors (NYSE:GM) Aren't Supporting the EV Turnaround\"\", 'General Motors CEO Mary Barra will be delivering the Opening Keynote at CES 2022', 'General Motors Silao Plant Workers To Vote On Union Contract This Week', 'General Motors sues Ford for violating trademarked driver-assist technology used for self-driving cars', 'General Motors, AT&T Partner For 5G Connectivity To Vehicles', 'General Motors to shut truck assembly plants again, cites global chip shortage', \"\"Ford vs GM legal battle: All about who wants to 'cruise'\"\", 'Why the Weak Retail Report Is Putting Pressure on Ford and General Motors', 'Several cars stolen from General Motors plant', 'General Motors (GM) Stock Is Plummeting 11.18% This Month: What Is Happening? – Own Snap', 'Auto News | ⚡General Motors To Recall Another 73,000 Chevrolet Bolt EVs Over Fire Risks', 'GM keeps large SUV, pickup trucks production going by parking 1,000 a day to await chips', 'Deutsche Bank says to buy General Motors now on post-earnings pullback', 'General Motors Files To Trademark Carbravo For Use With Dealers', 'General Motors announces massive profits in second quarter as new COVID-19 surge builds strength', 'General Motors Company (NYSE:GM) Low P/E Reflects the EV Transitory Risks', 'General Motors Can Achieve Record Profits If It Overcomes Delta Surge, Chip Shortage', 'GM workers in Mexico reject union in win for US free trade pact', 'Can General Motors Become an Electric Vehicle Leader?', 'General Motors recalls its Bolt model manufactured between 2017-19 owing to fire incidents', 'General Motors Raising EV Development Stakes, Barra Says', 'Premarket Movers Monday - Pfizer, Trillium, Uber and General Motors', 'General Motors Confirms New Commercial Electric Truck and Van', 'City works to build partnership with General Motors and explore transition to electric vehicles', 'General Motors and AT&T teaming up to launch 5G connected vehicles', 'General Motors (GM) Q2 2021 Earnings Call Transcript', 'GM holds onto its stake in troubled startup Lordstown Motors', 'GM to pause pickup production again because of chips shortage', 'GM to restart some production, but keep other plants idle amid chip shortage', 'GM Stock Is Rallying Into Earnings. Why They Better Be Good.', 'General Motors Co. stock falls Friday, underperforms market', 'Berkshire Trims General Motors Bet, Ramps Up Kroger Stake', 'GM Motors will resume production on August 23', \"\"Rock County Historical Society seeking General Motors items and stories for 'Rock County Legacies' project\"\", 'General Motors Co. stock falls Monday, underperforms market', 'General Motors (NYSE:GM) Spooks the Market Even After Raising the Guidance', 'General Motors Company (GM) Stock Declines -10.75% This Week; Should You Buy?', 'GM truck production back on next week after chip downtime', 'General Motors recalls all Chevrolet Volts worldwide due to fire risk – CBS Dallas / Fort Worth', 'General Motors Moves To Secure Its Own Critical Mineral Supply Chains', \"\"Still no fix as GM scrambles 'around the clock' to end Chevy Bolt battery fires\"\", 'GM to shut truck assembly plants again, cites global chip shortage', 'General Motors Stock Price Falls 4.7% – Time to Buy GM Stock?', 'General Motors hiring 100 workers for customer care facility', 'General Motors Co. stock rises Friday, outperforms market', 'General Motors Co. stock outperforms market on strong trading day', 'Bitcoin, PayPal, General Motors, the Fed and Jackson Hole: 5 Things You Must Know', 'General Motors is moving up a gear', 'General Motors Co. stock rises Wednesday, outperforms market', 'GM extends shutdown of Lansing Delta Township Assembly plant', 'Corvette Z06 Spied At The Nurburgring, Again: Video', 'Amazon hiring blitz for fulfillment center at former GM plant in Del. includes $3,000 bonuses', 'General Motors Company Looks Like It Could Be Ready To Breakout Soon - Benzinga', 'General Motors plans to exclusively offer electric vehicles by 2035', 'General Motors revamps logo to reflect drive towards \"\"all-electric future\"\"', 'General Motors Fort Wayne Truck Assembly to hold Electronic Recycling Day', 'Company Of The Day: General Motors', 'Toyota’s chip supply helps it beat General Motors for the first time', \"\"General Motors Says Maharashtra's Move To Block Its Exit May Hit Investment\"\", 'General Motors’ electric vehicle plan just got even more expensive', \"\"5 reasons General Motors' shares are trading at all-time highs\"\", 'Explainer: What has gone wrong at General Motors India plant?', 'GM and Ford cutting production at several North American plants due to chip shortage', 'Buffeted by Centre and State, General Motors threatens legal action', 'General Motors hit by chip shortage, to cut production at four plants', 'General Motors will start five plants it closed due to chip shortage', 'General Motors to shut its last factory in India on Christmas Eve', 'General Motors to recall 285,622 cars over faulty airbag warning lights', 'General Motors EV gamble could be Toyota’s gain as carmakers place bets', 'GM extending shutdowns at three car and crossover plants due to chip shortage', 'General Motors says worst of global chip shortage may be behind it', 'General Motors’ new Hummer EVs can drive diagonally', 'General Motors’ electric vehicle plan just got bigger, bolder, and more expensive', 'General Motors Will Sell Only Zero-Emission Vehicles, and Other News', 'General Motors looking at long-term supply contracts and partnerships for chips', 'GM To Make Only Electric Vehicles By 2035, Be Carbon Neutral By 2040', 'This Day In History: General Motors Acquires Chevrolet', 'General Motors to announce electric pickup at Detroit plant', 'General Motors to funnel $35bn into EVs by 2025', 'General Motors unveils Cadillac flying car and shuttle concepts at CES', 'G.M. Announcement Shakes Up U.S. Automakers’ Transition to Electric Cars', \"\"As World Wrestles With a Chip Shortage, GM's Plants Fire Back Up\"\", 'GM Rises As It Moves To Restock Dealer Lots, Updates Guidance', 'General Motors (GM) Breaks Out to All-Time High', 'General Motors signs deal to offer 60,000 EV charging points in US, Canada', 'From electric vehicles to air mobility: GM looks to grow beyond traditional auto industry', 'Despite Super Bowl Bragging, GM Is Part of Why U.S. Isn’t Beating Norway in EVs', 'General Motors recall 69,000 Bolt EVs for potential fire risk', 'General Motors to invest $71 million for new design, tech campus in California', 'General Motors Raises its Spending on Electric and Autonomous Vehicles, Pledges $35 Billion by 2025', 'General Motors expands China design studio to focus on EVs, smart cars', 'General Motors recalling all Chevy Bolt models due to fire risk', 'General Motors Company (GM) Stock Declines -10.75% This ...', 'General Motors Stock Slumps After $1 Billion Expanded ...', 'AT&T to provide zippy wireless to GM vehicles with eye on ...', 'Rock County Historical Society seeking General Motors items ...', 'GM Bolt Recall Sends Battery Maker Tumbling', 'General Motors recalls all Chevrolet Volts worldwide due to ...', 'Premarket Movers Monday - Pfizer, Trillium, Uber and General ...', 'General Motors (GM) Stock Is Plummeting 11.18% This Month ...', 'Stocks making the biggest moves premarket: Boeing ...', 'GM recalls all Chevy Bolts due to fire risk, says owners should ...', 'GM Recall Due to Fire Risk Covers All Chevrolet Bolts', \"\"GM and LG's too-big-to-fail ties tested by US$1 billion recall\"\", 'Bitcoin, PayPal, General Motors, Jackson Hole: 5 Things You ...', \"\"Shares of South Korea's LG Chem Sank After General Motors ...\"\", \"\"S. Korea's LG Chem shares dive on GM recall\"\", \"\"South Korea's LG Chem shares dive on GM electric car recall\"\", 'GM LG Chem Shares Slide as GM Expands Electric Vehicles ...', 'General Motors To Recall Another 73,000 Chevrolet Bolt EVs ...', 'General Motors loyalty still high in Flint, Mich.']"

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)
Feedback1="\"General Motors Recalls Newer Chevrolet Bolt EVs to Address BatteryFire Risks General Motors GM Misses Estimates on Chip Dearth Lifts FullYear Outlook General Motors to replace battery modules for some Bolt electric vehicles after fire risks General Motors to replace Chevrolet Camaro with an electric sedan Report Mediocre Returns on Capital At General Motors NYSEGM Arent Supporting the EV Turnaround General Motors CEO Mary Barra will be delivering the Opening Keynote at CES 2022 General Motors Silao Plant Workers To Vote On Union Contract This Week General Motors sues Ford for violating trademarked driverassist technology used for selfdriving cars General Motors ATT Partner For 5G Connectivity To Vehicles General Motors to shut truck assembly plants again cites global chip shortage Ford vs GM legal battle All about who wants to cruise Why the Weak Retail Report Is Putting Pressure on Ford and General Motors Several cars stolen from General Motors plant General Motors GM Stock Is Plummeting 1118 This Month What Is Happening – Own Snap Auto News |"
Feedback2="General Motors To Recall Another 73000 Chevrolet Bolt EVs Over Fire Risks GM keeps large SUV pickup trucks production going by parking 1000 a day to await chips Deutsche Bank says to buy General Motors now on postearnings pullback General Motors Files To Trademark Carbravo For Use With Dealers General Motors announces massive profits in second quarter as new COVID19 surge builds strength General Motors Company NYSEGM Low PE Reflects the EV Transitory Risks General Motors Can Achieve Record Profits If It Overcomes Delta Surge Chip Shortage GM workers in Mexico reject union in win for US free trade pact Can General Motors Become an Electric Vehicle Leader General Motors recalls its Bolt model manufactured between 201719 owing to fire incidents General Motors Raising EV Development Stakes Barra Says Premarket Movers Monday  Pfizer Trillium Uber and General Motors General Motors Confirms New Commercial Electric Truck and Van City works to build partnership with General Motors and explore transition to electric vehicles General Motors and ATT teaming up to launch 5G connected vehicles"
Feedback3="General Motors GM Q2 2021 Earnings Call Transcript GM holds onto its stake in troubled startup Lordstown Motors GM to pause pickup production again because of chips shortage GM to restart some production but keep other plants idle amid chip shortage GM Stock Is Rallying Into Earnings Why They Better Be Good General Motors Co stock falls Friday underperforms market Berkshire Trims General Motors Bet Ramps Up Kroger Stake GM Motors will resume production on August 23 Rock County Historical Society seeking General Motors items and stories for Rock County Legacies project General Motors Co stock falls Monday underperforms market General Motors NYSEGM Spooks the Market Even After Raising the Guidance General Motors Company GM Stock Declines 1075 This Week Should You Buy GM truck production back on next week after chip downtime General Motors recalls all Chevrolet Volts worldwide due to fire risk – CBS Dallas  Fort Worth General Motors Moves To Secure Its Own Critical Mineral Supply Chains Still no fix as GM scrambles around the clock to end Chevy Bolt battery fires GM to shut truck assembly plants again cites global chip shortage General Motors Stock Price Falls  "
Feedback4="This Week Should You Buy GM truck production back on next week after chip downtime General Motors recalls all Chevrolet Volts worldwide due to fire risk – CBS Dallas  Fort Worth General Motors Moves To Secure Its Own Critical Mineral Supply Chains Still no fix as GM scrambles around the clock to end Chevy Bolt battery fires GM to shut truck assembly plants again cites global chip shortage General Motors Stock Price Falls 47 – Time to Buy GM Stock General Motors hiring 100 workers for customer care facility General Motors Co stock rises Friday outperforms market General Motors Co stock outperforms market on strong trading day Bitcoin PayPal General Motors the Fed and Jackson Hole 5 Things You Must Know General Motors is moving up a gear General Motors Co stock rises Wednesday outperforms market GM extends shutdown of Lansing Delta Township Assembly plant Corvette Z06 Spied At The Nurburgring Again Video Amazon hiring blitz for fulfillment center at former GM plant in Del includes 3000 bonuses General Motors Company Looks Like It Could Be Ready To Breakout Soon  Benzinga General Motors plans to exclusively offer electric vehicles by 2035 General Motors"
Feedback5="future General Motors Fort Wayne Truck Assembly to hold Electronic Recycling Day Company Of The Day General Motors Toyota’s chip supply helps it beat General Motors for the first time General Motors Says Maharashtras Move To Block Its Exit May Hit Investment General Motors’ electric vehicle plan just got even more expensive 5 reasons General Motors shares are trading at alltime highs Explainer What has gone wrong at General Motors India plant GM and Ford cutting production at several North American plants due to chip shortage Buffeted by Centre and State General Motors threatens legal action General Motors hit by chip shortage to cut production at four plants General Motors will start five plants it closed due to chip shortage General Motors to shut its last factory in India on Christmas Eve General Motors to recall 285622 cars over faulty airbag warning lights General Motors EV gamble could be Toyota’s gain as carmakers place bets GM extending shutdowns at three car and crossover plants due to chip shortage General Motors says worst of global chip shortage may be behind it General Motors"
blob1=TextBlob(Feedback1)
blob2=TextBlob(Feedback2)
blob3=TextBlob(Feedback3)
blob4=TextBlob(Feedback4)
blob5=TextBlob(Feedback5)
print("--------------------------------------------------------")
print("Line 1")
print(blob1.sentiment)
print("--------------------------------------------------------")
print("Line 2")
print(blob2.sentiment)
print("--------------------------------------------------------")
print("Line 3")
print(blob3.sentiment)
print("--------------------------------------------------------")
print("Line 4")
print(blob4.sentiment)
print("--------------------------------------------------------")
print("Line 5")
print(blob5.sentiment)