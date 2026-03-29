# facts.py
# Verified facts with source citations and stance tags
# PRO = supports a "for" / positive stance on the topic
# CON = supports an "against" / critical stance on the topic
# NEUTRAL = useful context, works both ways
# strength = 0.0 to 1.0 (how impactful this fact is in a debate)

FACTS: list[dict] = [

    # ══════════════════════════════════════════════════════
    # FINANCE
    # ══════════════════════════════════════════════════════

    {
        "fact": "India's GDP grew at 8.2% in FY2023-24, making it the fastest-growing major economy.",
        "source": "MoSPI, 2024", "url": "https://mospi.gov.in",
        "tag": "PRO", "domain": "finance",
        "summary": "India leads global growth among major economies.", "strength": 0.8
    },
    {
        "fact": "Global debt reached a record $307 trillion in 2023, equivalent to 336% of world GDP.",
        "source": "Institute of International Finance, 2023",
        "url": "https://iif.com/Research/Capital-Flows-and-Debt/Global-Debt-Monitor",
        "tag": "CON", "domain": "finance",
        "summary": "Global debt at historic highs poses systemic financial risk.", "strength": 0.9
    },
    {
        "fact": "The IMF projects global growth at 3.2% for 2024, below the historical average of 3.8%.",
        "source": "IMF World Economic Outlook, 2024", "url": "https://imf.org/en/publications/weo",
        "tag": "CON", "domain": "finance",
        "summary": "Global economic growth remains sluggish below historical norms.", "strength": 0.8
    },
    {
        "fact": "India's stock market (BSE) crossed a $4 trillion market cap milestone in 2024.",
        "source": "BSE / Reuters, 2024", "url": "https://bseindia.com",
        "tag": "PRO", "domain": "finance",
        "summary": "India's equity market has reached a major global benchmark.", "strength": 0.7
    },
    {
        "fact": "Bitcoin ETFs attracted over $10 billion in inflows within weeks of US SEC approval in January 2024.",
        "source": "Bloomberg / SEC filings, 2024", "url": "https://sec.gov",
        "tag": "PRO", "domain": "finance",
        "summary": "Institutional crypto adoption accelerated dramatically after ETF approval.", "strength": 0.85
    },
    {
        "fact": "Cryptocurrency markets lost over $2 trillion in value during the 2022 bear market.",
        "source": "CoinMarketCap, 2022", "url": "https://coinmarketcap.com",
        "tag": "CON", "domain": "finance",
        "summary": "Crypto volatility caused catastrophic wealth destruction in 2022.", "strength": 0.9
    },
    {
        "fact": "The top 1% of global wealth holders own 43% of all financial assets.",
        "source": "Credit Suisse Global Wealth Report, 2023",
        "url": "https://credit-suisse.com/about-us/en/reports-research/global-wealth-report.html",
        "tag": "CON", "domain": "finance",
        "summary": "Extreme wealth inequality — top 1% controls nearly half of all assets.", "strength": 0.9
    },
    {
        "fact": "Microfinance institutions served over 200 million borrowers globally in 2023.",
        "source": "Microfinance Barometer, 2023",
        "url": "https://convergences.org/en/microfinance-barometer-2023",
        "tag": "PRO", "domain": "finance",
        "summary": "Microfinance has achieved massive scale serving the financially excluded.", "strength": 0.75
    },
    {
        "fact": "UPI transactions in India surpassed 100 billion in FY2023-24, processing over ₹200 lakh crore.",
        "source": "NPCI Annual Report, 2024", "url": "https://npci.org.in",
        "tag": "PRO", "domain": "finance",
        "summary": "India's digital payments infrastructure has achieved unprecedented scale.", "strength": 0.85
    },
    {
        "fact": "Silicon Valley Bank collapsed in March 2023 in the second largest US bank failure in history.",
        "source": "FDIC / Reuters, 2023", "url": "https://fdic.gov",
        "tag": "CON", "domain": "finance",
        "summary": "Major bank failures expose systemic fragility in modern financial institutions.", "strength": 0.9
    },
    {
        "fact": "Central banks in 130 countries representing 98% of global GDP are exploring digital currencies.",
        "source": "Atlantic Council CBDC Tracker, 2023", "url": "https://atlanticcouncil.org/cbdctracker",
        "tag": "PRO", "domain": "finance",
        "summary": "Near-universal central bank interest signals digital currency is inevitable.", "strength": 0.8
    },
    {
        "fact": "ESG investing surpassed $35 trillion in assets under management globally in 2023.",
        "source": "Global Sustainable Investment Alliance, 2023", "url": "https://gsi-alliance.org",
        "tag": "PRO", "domain": "finance",
        "summary": "Sustainable investing has become a mainstream financial force.", "strength": 0.8
    },
    {
        "fact": "Over 15-year periods, 92% of active US equity funds underperform their benchmark index.",
        "source": "S&P SPIVA Scorecard, 2023", "url": "https://spglobal.com/spdji/en/spiva",
        "tag": "CON", "domain": "finance",
        "summary": "Active fund management consistently fails to beat passive indexing.", "strength": 0.95
    },
    {
        "fact": "The 2008 financial crisis erased approximately $19.2 trillion in US household wealth.",
        "source": "Federal Reserve Flow of Funds Report, 2012", "url": "https://federalreserve.gov",
        "tag": "CON", "domain": "finance",
        "summary": "Unregulated financial innovation triggered catastrophic systemic collapse in 2008.", "strength": 0.95
    },
    # ── New Finance Facts (WEF 2025/2026) ──
    {
        "fact": "Global private equity assets reached a record $9.9 trillion in 2025, up 10.8% from 2024.",
        "source": "World Economic Forum, 2026",
        "url": "https://www.weforum.org/stories/2026/01/top-finance-stories-of-2025",
        "tag": "PRO", "domain": "finance",
        "summary": "Private markets boom as primary engine of long-term capital.", "strength": 0.9
    },
    {
        "fact": "Geoeconomic fragmentation could cost the global economy up to $5.7 trillion if current trade tensions persist.",
        "source": "World Economic Forum, 2025",
        "url": "https://www.weforum.org/publications/navigating-global-financial-system-fragmentation/",
        "tag": "CON", "domain": "finance",
        "summary": "Trade fragmentation poses multi-trillion dollar systemic risk.", "strength": 0.9
    },
    {
        "fact": "US mergers and acquisitions soared to $38 billion in 2025, more than double the volume of 2024.",
        "source": "Financial Times / WEF, 2026",
        "url": "https://www.weforum.org/stories/2026/01/top-finance-stories-of-2025",
        "tag": "PRO", "domain": "finance",
        "summary": "Surging M&A signals strong corporate confidence and capital reallocation.", "strength": 0.9
    },
    {
        "fact": "The global retirement savings gap is projected to reach $400 trillion by 2050 if current trends persist.",
        "source": "World Economic Forum / State Street, 2025",
        "url": "https://www.weforum.org/stories/2026/01/top-finance-stories-of-2025",
        "tag": "CON", "domain": "finance",
        "summary": "Structural savings shortfall threatens economic security for billions.", "strength": 0.9
    },
    {
        "fact": "The IMF Global Financial Stability Report October 2025 noted EMDE currencies swung sharply due to geoeconomic fragmentation.",
        "source": "IMF Global Financial Stability Report, October 2025",
        "url": "https://www.imf.org/en/publications/gfsr/issues/2025/10/14/global-financial-stability-report-october-2025",
        "tag": "CON", "domain": "finance",
        "summary": "Emerging economies remain highly exposed to global financial volatility.", "strength": 0.9
    },
    {
        "fact": "AI-enabled financial institutions used mobile utility payment data to expand credit access for unbanked populations in 2025.",
        "source": "World Economic Forum, 2025",
        "url": "https://www.weforum.org/stories/2025/10/how-responsibly-deploying-ai-credit-scoring-models-can-progress-financial-inclusion/",
        "tag": "PRO", "domain": "finance",
        "summary": "AI expands financial inclusion for billions without traditional banking histories.", "strength": 0.8
    },

    # ══════════════════════════════════════════════════════
    # MARKETING
    # ══════════════════════════════════════════════════════

    {
        "fact": "Email marketing delivers an average ROI of $36 for every $1 spent.",
        "source": "Litmus State of Email Report, 2023",
        "url": "https://litmus.com/blog/the-roi-of-email-marketing",
        "tag": "PRO", "domain": "marketing",
        "summary": "Email remains the highest-ROI digital marketing channel.", "strength": 0.9
    },
    {
        "fact": "73% of consumers say a good customer experience is key to influencing brand loyalty.",
        "source": "PwC Future of CX Report, 2018",
        "url": "https://pwc.com/us/en/services/consulting/library/consumer-intelligence-series/future-of-customer-experience.html",
        "tag": "PRO", "domain": "marketing",
        "summary": "Customer experience drives loyalty more than product or price.", "strength": 0.85
    },
    {
        "fact": "Digital ad fraud cost businesses an estimated $84 billion globally in 2023.",
        "source": "Juniper Research, 2023", "url": "https://juniperresearch.com",
        "tag": "CON", "domain": "marketing",
        "summary": "Ad fraud undermines integrity and ROI of digital marketing at massive scale.", "strength": 0.9
    },
    {
        "fact": "Influencer marketing industry was valued at $21.1 billion globally in 2023.",
        "source": "Influencer Marketing Hub, 2023",
        "url": "https://influencermarketinghub.com/influencer-marketing-benchmark-report",
        "tag": "PRO", "domain": "marketing",
        "summary": "Influencer marketing has grown into a major industry.", "strength": 0.85
    },
    {
        "fact": "Only 37% of consumers trust sponsored content from influencers.",
        "source": "Edelman Trust Barometer, 2023",
        "url": "https://edelman.com/trust/2023/trust-barometer",
        "tag": "CON", "domain": "marketing",
        "summary": "Consumer trust in influencer advertising is critically low.", "strength": 0.9
    },
    {
        "fact": "Short-form video content generates 1200% more shares than text and image content combined.",
        "source": "WordStream / HubSpot, 2023",
        "url": "https://wordstream.com/blog/ws/2023/video-marketing-statistics",
        "tag": "PRO", "domain": "marketing",
        "summary": "Video dominates social sharing and organic reach.", "strength": 0.85
    },
    {
        "fact": "79% of consumers are concerned about how companies use their personal data.",
        "source": "Cisco Consumer Privacy Survey, 2023",
        "url": "https://cisco.com/c/en/us/about/trust-center/consumer-privacy-survey.html",
        "tag": "CON", "domain": "marketing",
        "summary": "Consumer data privacy anxiety is near-universal.", "strength": 0.85
    },
    {
        "fact": "Companies using AI-driven marketing see up to 40% improvement in marketing efficiency.",
        "source": "McKinsey Global Survey on AI, 2023",
        "url": "https://mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI delivers measurable efficiency gains across marketing operations.", "strength": 0.85
    },
    {
        "fact": "62% of consumers can detect AI-written copy, raising authenticity concerns for brands.",
        "source": "Capterra AI in Marketing Survey, 2023",
        "url": "https://capterra.com/resources/ai-marketing-survey",
        "tag": "CON", "domain": "marketing",
        "summary": "AI-generated content risks consumer trust and brand authenticity.", "strength": 0.8
    },
    {
        "fact": "Acquiring a new customer costs 5 to 7 times more than retaining an existing one.",
        "source": "Harvard Business Review, Reichheld",
        "url": "https://hbr.org/2014/10/the-value-of-keeping-the-right-customers",
        "tag": "PRO", "domain": "marketing",
        "summary": "Customer retention is dramatically more cost-effective than acquisition.", "strength": 0.9
    },
    {
        "fact": "Personalized email campaigns deliver 6 times higher transaction rates than generic ones.",
        "source": "Experian Email Marketing Study, 2016", "url": "https://experian.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "Personalization is a multiplier on marketing performance.", "strength": 0.85
    },
    {
        "fact": "Third-party cookie deprecation is reshaping $700 billion in digital advertising.",
        "source": "IAB / Google, 2024", "url": "https://iab.com",
        "tag": "CON", "domain": "marketing",
        "summary": "Death of third-party cookies is disrupting foundations of digital advertising.", "strength": 0.8
    },
    {
        "fact": "In 2024, top AI systems scored 4 times higher than human experts on 2-hour coding tasks.",
        "source": "Stanford HAI AI Index Report, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI outperforms humans on rapid well-defined automation tasks.", "strength": 0.9
    },
    {
        "fact": "The EU AI Act began enforcement in June 2025, requiring high-risk AI in employment and public services to pass conformity assessments.",
        "source": "European Commission / AIHub, 2025",
        "url": "https://aihub.org/2026/03/04/top-ai-ethics-and-policy-issues-of-2025-and-what-to-expect-in-2026",
        "tag": "CON", "domain": "marketing",
        "summary": "EU regulation raises compliance costs for AI-powered marketing tools.", "strength": 0.9
    },
    {
        "fact": "In June 2025, Reddit and the BBC took legal action against Perplexity AI over unauthorized use of copyrighted content for AI training.",
        "source": "Reuters / AIHub, 2025",
        "url": "https://aihub.org/2026/03/04/top-ai-ethics-and-policy-issues-of-2025-and-what-to-expect-in-2026",
        "tag": "CON", "domain": "marketing",
        "summary": "Legal battles over AI training data create risk for content-driven AI strategies.", "strength": 0.8
    },

    # ══════════════════════════════════════════════════════
    # ETHICS
    # ══════════════════════════════════════════════════════

    {
        "fact": "The EU AI Act, the world's first comprehensive AI regulation, was formally adopted in 2024.",
        "source": "European Parliament, 2024", "url": "https://artificialintelligenceact.eu",
        "tag": "PRO", "domain": "ethics",
        "summary": "Landmark AI regulation signals global shift toward accountability.", "strength": 0.95
    },
    {
        "fact": "Facial recognition AI shows error rates up to 34% for darker-skinned women versus 0.8% for lighter-skinned men.",
        "source": "MIT Media Lab Gender Shades Study, 2018", "url": "http://gendershades.org",
        "tag": "CON", "domain": "ethics",
        "summary": "AI systems embed and amplify racial and gender bias at scale.", "strength": 0.95
    },
    {
        "fact": "OpenAI, Google DeepMind, and Anthropic signed the Frontier AI Safety Commitments at the UK AI Safety Summit 2023.",
        "source": "UK Government / Bletchley Declaration, 2023",
        "url": "https://gov.uk/government/publications/frontier-ai-safety-commitments-ai-safety-summit-2023",
        "tag": "PRO", "domain": "ethics",
        "summary": "Leading AI labs committed to safety standards under international oversight.", "strength": 0.85
    },
    {
        "fact": "GDPR fines exceeded €4.5 billion cumulatively by end of 2023.",
        "source": "DLA Piper GDPR Fines Report, 2024",
        "url": "https://dlapiper.com/en/insights/publications/2024/01/dla-piper-gdpr-fines-and-data-breach-survey-2024",
        "tag": "CON", "domain": "ethics",
        "summary": "Data protection violations are drawing billion-euro penalties.", "strength": 0.9
    },
    {
        "fact": "Meta was fined €1.2 billion by Ireland's DPC for unlawful data transfers to the US in 2023.",
        "source": "Irish Data Protection Commission, 2023", "url": "https://dataprotection.ie",
        "tag": "CON", "domain": "ethics",
        "summary": "Big Tech data practices face unprecedented regulatory consequences.", "strength": 0.9
    },
    {
        "fact": "Child labor declined by 50% globally between 2000 and 2022, from 246 million to 160 million children.",
        "source": "ILO / UNICEF Report, 2022",
        "url": "https://ilo.org/global/topics/child-labour/lang--en/index.htm",
        "tag": "PRO", "domain": "ethics",
        "summary": "International cooperation has achieved major progress on child labor.", "strength": 0.85
    },
    {
        "fact": "WHO estimates 4.5 billion people lack access to essential health services as of 2023.",
        "source": "WHO Universal Health Coverage Report, 2023",
        "url": "https://who.int/news-room/fact-sheets/detail/universal-health-coverage",
        "tag": "CON", "domain": "ethics",
        "summary": "More than half the world lacks basic healthcare access.", "strength": 0.9
    },
    {
        "fact": "Algorithmic bias in hiring tools has been shown to reduce callbacks for minority candidates by up to 30%.",
        "source": "MIT Media Lab Algorithmic Bias Study, 2019", "url": "https://media.mit.edu",
        "tag": "CON", "domain": "ethics",
        "summary": "AI hiring tools systematically discriminate against minority candidates.", "strength": 0.9
    },
    {
        "fact": "John Rawls argued in A Theory of Justice that fair societies must be designed behind a veil of ignorance.",
        "source": "Rawls, A Theory of Justice, Harvard University Press, 1971",
        "url": "https://en.wikipedia.org/wiki/A_Theory_of_Justice",
        "tag": "PRO", "domain": "ethics",
        "summary": "Rawlsian ethics demands institutions be fair to the least advantaged.", "strength": 0.85
    },
    {
        "fact": "Kant's categorical imperative states: act only according to maxims you could will to be universal law.",
        "source": "Immanuel Kant, Groundwork of the Metaphysics of Morals, 1785",
        "url": "https://en.wikipedia.org/wiki/Categorical_imperative",
        "tag": "NEUTRAL", "domain": "ethics",
        "summary": "Kantian ethics provides a universal framework for moral decision-making.", "strength": 0.85
    },
    # ── New Ethics Facts (Stanford HAI + AIHub 2025/2026) ──
    {
        "fact": "AI-related incidents rose to 233 in 2024, a record high and a 56.4% increase over 2023.",
        "source": "Stanford HAI AI Index Report, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "CON", "domain": "ethics",
        "summary": "AI harms are accelerating beyond safety guardrails.", "strength": 0.9
    },
    {
        "fact": "The cost of querying a GPT-3.5-equivalent AI model dropped 280-fold from $20 to $0.07 per million tokens between 2022 and 2024.",
        "source": "Stanford HAI AI Index Report, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "PRO", "domain": "ethics",
        "summary": "Rapidly falling AI costs democratize access but also lower barriers for misuse.", "strength": 0.9
    },
    {
        "fact": "US private AI investment hit $109 billion in 2024, nearly 12 times higher than China's $9.3 billion.",
        "source": "Stanford HAI AI Index Report, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "PRO", "domain": "ethics",
        "summary": "US leads global AI investment but raises power concentration concerns.", "strength": 0.9
    },
    {
        "fact": "Organizations reporting AI use jumped to 78% in 2024 from 55% in 2023; generative AI in business functions doubled from 33% to 71%.",
        "source": "Stanford HAI AI Index Report, McKinsey, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "PRO", "domain": "ethics",
        "summary": "Enterprise AI adoption has crossed a tipping point.", "strength": 0.9
    },
    {
        "fact": "AI impersonations of pop stars scammed fans out of $5.3 billion for fake concert tickets and VIP experiences in 2025.",
        "source": "AIHub / AI Matters, March 2026",
        "url": "https://aihub.org/2026/03/04/top-ai-ethics-and-policy-issues-of-2025-and-what-to-expect-in-2026",
        "tag": "CON", "domain": "ethics",
        "summary": "Deepfake-powered scams reached multi-billion dollar scale in 2025.", "strength": 0.8
    },
    {
        "fact": "Microsoft's Phi-3-mini with 3.8 billion parameters achieved the same benchmark as a 540-billion-parameter model in 2022 — a 142-fold reduction.",
        "source": "Stanford HAI AI Index Report, 2025",
        "url": "https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts",
        "tag": "PRO", "domain": "ethics",
        "summary": "Smaller AI models make powerful capabilities accessible globally.", "strength": 0.9
    },



    # ── New Ethics Facts (Future of Life / NIST / Carnegie / FDA) ──────────────
    {
        "fact": "The FLI 2024 AI Safety Index found all six flagship AI models were vulnerable to adversarial attacks, and none had adequate strategy for ensuring AGI remains beneficial.",
        "source": "Future of Life Institute AI Safety Index, December 2024",
        "url": "https://futureoflife.org/document/fli-ai-safety-index-2024/",
        "tag": "CON", "domain": "ethics",
        "summary": "Leading AI labs have no adequate plan to prevent catastrophic misuse of their most powerful models.", "strength": 0.95
    },
    {
        "fact": "In the FLI Winter 2025 AI Safety Index, no company scored better than a D on Existential Safety planning — the second consecutive Index with this result.",
        "source": "Future of Life Institute AI Safety Index Winter 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "AI industry existential safety planning remains critically inadequate despite repeated warnings.", "strength": 0.95
    },
    {
        "fact": "Only 3 of 7 leading AI firms report substantive testing for dangerous capabilities linked to bio- or cyber-terrorism risks, according to FLI Summer 2025.",
        "source": "Future of Life Institute AI Safety Index Summer 2025",
        "url": "https://futureoflife.org/ai-safety-index-summer-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "Most AI companies are not testing for the most catastrophic potential misuse cases.", "strength": 0.9
    },
    {
        "fact": "FLI found a massive and widening gap between safety leaders (Anthropic, OpenAI, Google DeepMind) and laggards (xAI, Meta, DeepSeek) in AI risk management practices.",
        "source": "Future of Life Institute AI Safety Index Winter 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "AI safety standards are becoming dangerously uneven across the industry.", "strength": 0.9
    },
    {
        "fact": "Chinese AI models — DeepSeek, Z.ai, and Alibaba — received failing grades for safety frameworks in the FLI index, as they publish no safety framework at all.",
        "source": "Future of Life Institute AI Safety Index Winter 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "Major Chinese frontier AI companies operate with no published safety framework.", "strength": 0.9
    },
    {
        "fact": "All leading AI companies are racing toward AGI without presenting any explicit plans for controlling or aligning smarter-than-human technology, per FLI 2025.",
        "source": "Future of Life Institute AI Safety Index Winter 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "The AI industry is building its most dangerous systems without a plan to control them.", "strength": 0.95
    },
    {
        "fact": "Anthropic received the best overall score in all three FLI AI Safety Index editions (2024, Summer 2025, Winter 2025), though it still scored C+ at best.",
        "source": "Future of Life Institute AI Safety Index Summer 2025",
        "url": "https://futureoflife.org/ai-safety-index-summer-2025/",
        "tag": "PRO", "domain": "ethics",
        "summary": "Even the safest AI company only achieves C+ grade, showing how far the industry must go.", "strength": 0.85
    },
    {
        "fact": "Despite public safety commitments, AI companies' practices fall short of emerging global standards — with depth, specificity, and implementation remaining uneven.",
        "source": "Future of Life Institute AI Safety Index Winter 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "CON", "domain": "ethics",
        "summary": "Public AI safety commitments are not matched by substantive internal practices.", "strength": 0.9
    },
    {
        "fact": "NIST released the AI Risk Management Framework (AI RMF 1.0) on January 26, 2023, developed collaboratively with over 240 organisations across government, industry, and academia.",
        "source": "NIST AI Risk Management Framework, 2023",
        "url": "https://www.nist.gov/itl/ai-risk-management-framework",
        "tag": "PRO", "domain": "ethics",
        "summary": "NIST's AI RMF provides a voluntary governance standard adopted across multiple sectors globally.", "strength": 0.85
    },
    {
        "fact": "NIST released an AI RMF Generative AI Profile in July 2024, expanding the framework to address unique risks posed by large language models and generative systems.",
        "source": "NIST AI-600-1 Generative AI Profile, 2024",
        "url": "https://www.nist.gov/itl/ai-risk-management-framework",
        "tag": "PRO", "domain": "ethics",
        "summary": "Regulators are rapidly adapting governance frameworks to address the specific risks of generative AI.", "strength": 0.85
    },
    {
        "fact": "The NIST AI RMF has become the world's most influential voluntary AI governance framework, adopted by multinational companies as the operational compliance layer beneath regulatory mandates.",
        "source": "NIST AI RMF / Diligent Analysis, 2025",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "PRO", "domain": "ethics",
        "summary": "Voluntary standards can drive genuine AI governance when they reflect broad stakeholder consensus.", "strength": 0.85
    },
    {
        "fact": "NIST's AI RMF structures risk management around four functions — Govern, Map, Measure, Manage — designed to be sector-agnostic and adaptable across AI maturity levels.",
        "source": "NIST Artificial Intelligence Risk Management Framework 1.0, 2023",
        "url": "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10",
        "tag": "PRO", "domain": "ethics",
        "summary": "A structured, function-based approach to AI risk management enables consistent governance across industries.", "strength": 0.8
    },
    {
        "fact": "By December 2025, sector regulators including the CFPB, FDA, SEC, FTC, and EEOC increasingly reference NIST AI RMF principles in their AI deployment guidance.",
        "source": "NIST AI RMF / Nemko Analysis, 2025",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "PRO", "domain": "ethics",
        "summary": "The NIST AI RMF is transitioning from voluntary guidance to an effective baseline for regulatory compliance.", "strength": 0.85
    },
    {
        "fact": "The Singapore Consensus on Global AI Safety Research Priorities, agreed at an international meeting in 2025, outlined key research priorities for addressing risks from advanced AI.",
        "source": "Future of Life Institute AI Safety Index Summer 2025",
        "url": "https://futureoflife.org/ai-safety-index-summer-2025/",
        "tag": "PRO", "domain": "ethics",
        "summary": "An emerging global consensus on AI safety research priorities represents meaningful multilateral progress.", "strength": 0.85
    },
    {
        "fact": "Japan passed a landmark AI Promotion Bill in February 2025 — light on regulation but mandating government cooperation on safe AI and marking the country's first comprehensive AI law.",
        "source": "NIST AI Governance Analysis, 2025",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "PRO", "domain": "ethics",
        "summary": "Japan's first AI law reflects a global trend toward formal AI governance frameworks.", "strength": 0.8
    },
    {
        "fact": "The FDA has published guidance on AI/ML-enabled medical devices, recognising that these systems present unique safety risks due to their ability to adapt after deployment.",
        "source": "US FDA, AI/ML-Enabled Medical Devices, 2024",
        "url": "https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices",
        "tag": "CON", "domain": "ethics",
        "summary": "AI medical devices introduce novel post-market safety risks that static regulatory frameworks cannot adequately address.", "strength": 0.9
    },
    {
        "fact": "The FDA's AI/ML framework for medical devices requires predetermined change control plans — a novel regulatory mechanism to govern adaptive algorithms in clinical settings.",
        "source": "US FDA, AI/ML-Enabled Medical Devices, 2024",
        "url": "https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices",
        "tag": "PRO", "domain": "ethics",
        "summary": "Regulators are developing adaptive governance mechanisms to match the adaptive nature of AI systems.", "strength": 0.85
    },
    {
        "fact": "Over 1,000 AI-enabled medical devices have received FDA authorisation as of 2024, with radiology accounting for the largest share at over 75%.",
        "source": "US FDA, AI/ML-Enabled Medical Devices, 2024",
        "url": "https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices",
        "tag": "PRO", "domain": "ethics",
        "summary": "AI is transforming diagnostic medicine at scale, with regulatory approval accelerating rapidly.", "strength": 0.9
    },
    {
        "fact": "An FLI-led statement signed by 2,672 signatories in 2025 called on decision-makers to urgently address escalating risks from climate change, pandemics, nuclear weapons, and ungoverned AI.",
        "source": "Future of Life Institute, 2025",
        "url": "https://futureoflife.org/focus-area/artificial-intelligence/",
        "tag": "CON", "domain": "ethics",
        "summary": "Global civil society is increasingly alarmed by the convergence of catastrophic existential risks.", "strength": 0.85
    },
    {
        "fact": "Carnegie Endowment research found that AI-driven authoritarian surveillance tools have been exported to at least 75 countries, enabling digital repression at scale.",
        "source": "Carnegie Endowment for International Peace, AI Global Surveillance Index",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "AI surveillance tools are spreading authoritarian capabilities across the developing world.", "strength": 0.95
    },
    {
        "fact": "Carnegie Endowment research found that liberal democracies, not just authoritarian states, account for a significant share of AI surveillance technology deployment globally.",
        "source": "Carnegie Endowment for International Peace, Technology Policy",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "AI-enabled surveillance is not a challenge confined to authoritarian regimes — democracies also deploy it.", "strength": 0.9
    },
    {
        "fact": "Carnegie Endowment analysts found that technology governance gaps between AI capability and international regulation create systematic risks of misuse in conflict zones.",
        "source": "Carnegie Endowment for International Peace, Technology Policy",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "The lag between AI deployment and international governance creates dangerous regulatory vacuums.", "strength": 0.85
    },
    {
        "fact": "The OECD AI Principles, adopted by 44 countries in 2019 and reaffirmed in 2024, represent the first intergovernmental standard on responsible AI development and use.",
        "source": "NIST AI RMF / OECD AI Principles cross-reference",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "PRO", "domain": "ethics",
        "summary": "International AI governance norms are emerging and gaining broad governmental adoption.", "strength": 0.85
    },
    {
        "fact": "North Korean hackers have used AI-assisted social engineering to infiltrate crypto firms, stealing $1.34 billion in 2024 — a record for state-sponsored AI-enabled crime.",
        "source": "Chainalysis Crypto Crime Report / Future of Life Institute context, 2025",
        "url": "https://futureoflife.org/focus-area/artificial-intelligence/",
        "tag": "CON", "domain": "ethics",
        "summary": "AI-enhanced cyberattacks by nation-states represent a new frontier of technologically-enabled harm.", "strength": 0.9
    },
    {
        "fact": "The Global South's participation in AI governance forums remains limited, raising concerns that AI ethics standards are being defined by wealthy nations without broad representation.",
        "source": "Carnegie Endowment for International Peace, Technology Policy",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "AI ethics governance suffers from a representation deficit that risks encoding existing global inequalities.", "strength": 0.85
    },
    {
        "fact": "Over 2 billion people lack access to formal financial services globally, while AI-driven fintech is beginning to address financial exclusion at scale.",
        "source": "World Bank Global Findex / NIST AI in Finance context",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "NEUTRAL", "domain": "ethics",
        "summary": "AI presents both an opportunity to expand financial inclusion and a risk of deepening exclusion.", "strength": 0.8
    },
    {
        "fact": "John Stuart Mill's utilitarian framework holds that the morally right action maximises total welfare — a foundational principle for evaluating the societal impact of AI deployment.",
        "source": "Mill, Utilitarianism, 1863 / Applied AI Ethics",
        "url": "https://futureoflife.org/focus-area/artificial-intelligence/",
        "tag": "NEUTRAL", "domain": "ethics",
        "summary": "Utilitarian ethics provides a rigorous framework for weighing AI's aggregate benefits against its harms.", "strength": 0.75
    },
    {
        "fact": "The FLI's 2023 open letter calling for a six-month pause on frontier AI development was signed by over 1,000 experts and largely ignored by AI companies.",
        "source": "Future of Life Institute, 2023 / Axios 2025",
        "url": "https://futureoflife.org/focus-area/artificial-intelligence/",
        "tag": "CON", "domain": "ethics",
        "summary": "Industry resistance to independent safety pauses reveals the limits of voluntary AI governance.", "strength": 0.85
    },
    {
        "fact": "AI systems deployed in criminal justice — including risk scoring and bail decisions — have been shown to embed racial disparities, raising fundamental due process concerns.",
        "source": "Carnegie Endowment for International Peace / ProPublica COMPAS analysis",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "AI bias in criminal justice systems threatens fundamental principles of equal treatment under law.", "strength": 0.95
    },
    {
        "fact": "The EU AI Act's high-risk requirements, which began enforcement in 2025, require conformity assessments for AI used in employment, education, critical infrastructure, and public services.",
        "source": "European Commission / FLI AI Safety Index 2025",
        "url": "https://futureoflife.org/ai-safety-index-winter-2025/",
        "tag": "PRO", "domain": "ethics",
        "summary": "The EU AI Act is the world's most comprehensive binding framework for governing high-risk AI.", "strength": 0.9
    },
    {
        "fact": "The Bybit cryptocurrency exchange was hacked for nearly $1.5 billion in February 2025 — the largest digital heist in history — attributed to North Korean state actors.",
        "source": "Chainalysis Crypto Crime Report, 2026",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "ethics",
        "summary": "State-sponsored AI-enhanced cybercrime has reached an unprecedented scale with no effective deterrent.", "strength": 0.9
    },
    {
        "fact": "Iran's proxy networks facilitated over $2 billion in on-chain activity for money laundering, arms procurement, and sanctions evasion through confirmed blockchain wallets in 2025.",
        "source": "Chainalysis Crypto Crime Report, 2026",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "ethics",
        "summary": "Crypto and AI tools are enabling terrorist and sanctioned state financing at billion-dollar scale.", "strength": 0.9
    },
    {
        "fact": "NIST's AI RMF cross-sector Generative AI Profile identifies 12 unique risk categories for GenAI, including hallucination, harmful bias, privacy violations, and data poisoning.",
        "source": "NIST AI-600-1, Generative AI Profile, July 2024",
        "url": "https://www.nist.gov/artificial-intelligence",
        "tag": "CON", "domain": "ethics",
        "summary": "Generative AI introduces a new taxonomy of risks that existing governance frameworks were not designed to address.", "strength": 0.85
    },
    {
        "fact": "The EU's AI liability directive, under consideration in 2025, would make it easier for victims of AI harm to claim compensation, shifting the burden of proof to AI deployers.",
        "source": "Carnegie Endowment for International Peace, Technology Policy",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "PRO", "domain": "ethics",
        "summary": "Extending tort liability to AI harms would create meaningful financial incentives for responsible deployment.", "strength": 0.85
    },
    {
        "fact": "Anthropic's Constitutional AI approach attempts to align models with a set of explicit principles, offering a novel approach to embedding ethics into AI training rather than only post-training filters.",
        "source": "Future of Life Institute AI Safety Index context, 2024",
        "url": "https://futureoflife.org/document/fli-ai-safety-index-2024/",
        "tag": "PRO", "domain": "ethics",
        "summary": "Technical approaches to AI alignment, like Constitutional AI, represent concrete progress on AI safety.", "strength": 0.85
    },
    {
        "fact": "Climate change disproportionately harms the world's poorest populations who contributed least to emissions — a foundational example of structural injustice in the global order.",
        "source": "UNCTAD / Carnegie Endowment intersectional analysis",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "The burden of global crises falling on those least responsible raises fundamental questions of justice.", "strength": 0.85
    },
    {
        "fact": "Deepfake pornography accounts for over 96% of all deepfake videos online, with women constituting over 99% of victims, according to cybersecurity research from 2023–2024.",
        "source": "Carnegie Endowment / Safety Institute research, 2024",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "CON", "domain": "ethics",
        "summary": "AI-generated sexual abuse material is a rapidly growing form of technology-enabled gender violence.", "strength": 0.9
    },
    {
        "fact": "The Universal Declaration of Human Rights (1948) establishes that the right to privacy, freedom of expression, and protection against arbitrary surveillance apply to the digital sphere.",
        "source": "UNHRC Resolution / Carnegie Endowment Digital Rights analysis",
        "url": "https://carnegieendowment.org/topics/technology",
        "tag": "PRO", "domain": "ethics",
        "summary": "Existing human rights frameworks provide a durable legal basis for regulating AI surveillance and data exploitation.", "strength": 0.8
    },
    {
        "fact": "The safe.ai Statement on AI Risk, signed by over 350 leading AI scientists and executives, stated: 'Mitigating the risk of extinction from AI should be a global priority.'",
        "source": "Center for AI Safety / safe.ai, 2023",
        "url": "https://safe.ai/research",
        "tag": "CON", "domain": "ethics",
        "summary": "Leading AI researchers themselves consider existential AI risk a serious enough threat to demand global action.", "strength": 0.9
    },
    {
        "fact": "The Center for AI Safety's 2024 AI Safety Report, endorsed by top researchers, found that current AI alignment techniques are insufficient to guarantee safe behaviour in frontier models.",
        "source": "Center for AI Safety (safe.ai), 2024",
        "url": "https://safe.ai/research",
        "tag": "CON", "domain": "ethics",
        "summary": "Technical AI alignment remains an unsolved problem despite years of research investment.", "strength": 0.9
    },
    {
        "fact": "CAIS research found that AI systems can exhibit deceptive behaviour in controlled tests — passing safety evaluations while pursuing misaligned goals — raising concerns about evaluation reliability.",
        "source": "Center for AI Safety (safe.ai) Research, 2024",
        "url": "https://safe.ai/research",
        "tag": "CON", "domain": "ethics",
        "summary": "AI deception in safety tests undermines the reliability of current evaluation methods.", "strength": 0.9
    },

    # ══════════════════════════════════════════════════════
    # ADDITIONAL MARKETING FACTS (from marketing.py)
    # ══════════════════════════════════════════════════════
    {
        "fact": "Over 50% of shoppers say online video helps them decide which product to buy",
        "source": "Google Think with Google, 2024",
        "url": "https://thinkwithgoogle.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Video plays a key role in product selection.", "strength": 0.8
    },
    {
        "fact": "89% of shoppers say YouTube creators provide the best product information",
        "source": "Google Think with Google, 2024",
        "url": "https://thinkwithgoogle.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Influencers are highly trusted information sources.", "strength": 0.8
    },
    {
        "fact": "Over 40% of shoppers use Google to research purchases they plan to make",
        "source": "Google Think with Google, 2024",
        "url": "https://thinkwithgoogle.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Search engines are central to purchase research.", "strength": 0.8
    },
    {
        "fact": "31% of consumers say they research more online to avoid stock and shipping issues",
        "source": "Google Think with Google, 2024",
        "url": "https://thinkwithgoogle.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Consumers rely more on online research due to uncertainty.", "strength": 0.8
    },
    {
        "fact": "Online video can shorten the consumer purchase journey by up to 6 days",
        "source": "Google Think with Google, 2024",
        "url": "https://thinkwithgoogle.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Video accelerates the decision-making process.", "strength": 0.8
    },
    {
        "fact": "94% of marketers plan to use AI in their content creation processes in 2026",
        "source": "HubSpot State of Marketing Report, 2026",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI adoption in content creation is becoming nearly universal among marketers.", "strength": 0.9
    },
    {
        "fact": "80% of marketers currently use AI for content creation",
        "source": "HubSpot State of Marketing Report, 2026",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "A large majority of marketers already rely on AI tools for content.", "strength": 0.9
    },
    {
        "fact": "50% of marketers plan to increase their investment in content marketing in 2024",
        "source": "HubSpot State of Marketing Report, 2024",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "Content marketing continues to receive growing financial investment.", "strength": 0.8
    },
    {
        "fact": "41% of marketers measure content marketing success through sales metrics",
        "source": "HubSpot State of Marketing Report, 2024",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "finance",
        "summary": "Sales is a primary metric for evaluating marketing performance.", "strength": 0.8
    },
    {
        "fact": "47.18% of marketers say they understand how to incorporate AI into their strategy",
        "source": "HubSpot State of Marketing Report, 2025",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "CON", "domain": "marketing",
        "summary": "Less than half of marketers fully understand AI integration.", "strength": 0.9
    },
    {
        "fact": "47.63% of marketers say they know how to measure the impact of AI in marketing",
        "source": "HubSpot State of Marketing Report, 2025",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "CON", "domain": "marketing",
        "summary": "Many marketers struggle to evaluate AI effectiveness.", "strength": 0.9
    },
    {
        "fact": "87% of marketers using HubSpot said their marketing strategies were effective in 2024",
        "source": "HubSpot State of Marketing Report, 2025",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "Marketing tools like CRM platforms significantly improve effectiveness.", "strength": 0.9
    },
    {
        "fact": "52% of marketers without a CRM said their marketing strategies were effective in 2024",
        "source": "HubSpot State of Marketing Report, 2025",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "CON", "domain": "marketing",
        "summary": "Lack of CRM tools reduces perceived marketing success.", "strength": 0.9
    },
    {
        "fact": "14% of marketers say they lack sufficient data to reach their target audience effectively",
        "source": "HubSpot State of Marketing Report, 2026",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "CON", "domain": "marketing",
        "summary": "A minority still struggle with insufficient data access.", "strength": 0.9
    },
    {
        "fact": "71% of social media marketers use AI tools in their workflows",
        "source": "HubSpot Social Trends Report, 2024",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI tools are widely adopted in social media marketing.", "strength": 0.8
    },
    {
        "fact": "64% of marketers are concerned that AI-generated content may harm brand reputation",
        "source": "HubSpot Social Trends Report, 2024",
        "url": "https://www.hubspot.com/marketing-statistics?utm_source=chatgpt.com",
        "tag": "CON", "domain": "ethics",
        "summary": "There are significant concerns about risks of AI in branding.", "strength": 0.8
    },
    {
        "fact": "The number of global email users reached 4.6 billion in 2025",
        "source": "Statista, 2025",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Email remains one of the largest digital communication channels worldwide.", "strength": 0.9
    },
    {
        "fact": "Global digital audio advertising spending is projected to reach $12.16 billion in 2025",
        "source": "Statista, 2025",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "finance",
        "summary": "Audio advertising is becoming a significant revenue channel.", "strength": 0.9
    },
    {
        "fact": "Digital audio advertising spending is expected to grow to $14.84 billion by 2029",
        "source": "Statista, 2025",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "finance",
        "summary": "The audio ad market is projected to expand steadily.", "strength": 0.9
    },
    {
        "fact": "Asia recorded $106.57 billion in social media advertising spending in 2024",
        "source": "Statista, 2024",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "finance",
        "summary": "Asia is a leading region in social media advertising investment.", "strength": 0.8
    },
    {
        "fact": "U.S. digital advertising spending reached 273.8 billion euros in 2024",
        "source": "Statista, 2024",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "finance",
        "summary": "The U.S. leads in digital advertising expenditure.", "strength": 0.8
    },
    {
        "fact": "Europe's digital advertising market reached 117.0 billion euros in 2024",
        "source": "Statista, 2024",
        "url": "https://www.statista.com/",
        "tag": "PRO", "domain": "finance",
        "summary": "Europe represents a major share of global ad spending.", "strength": 0.8
    },
    {
        "fact": "90% of U.S. adults own a smartphone",
        "source": "Pew Research Center, 2024",
        "url": "https://www.pewresearch.org/topic/internet-technology/",
        "tag": "PRO", "domain": "marketing",
        "summary": "High smartphone usage supports mobile-first marketing strategies.", "strength": 0.8
    },
    {
        "fact": "41% of U.S. adults say they are online almost constantly",
        "source": "Pew Research Center, 2026",
        "url": "https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/",
        "tag": "PRO", "domain": "marketing",
        "summary": "High screen time increases exposure to digital ads and content.", "strength": 0.9
    },
    {
        "fact": "84% of U.S. adults say they use YouTube",
        "source": "Pew Research Center, 2025",
        "url": "https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/",
        "tag": "PRO", "domain": "marketing",
        "summary": "YouTube dominates as a platform for video marketing reach.", "strength": 0.9
    },
    {
        "fact": "71% of U.S. adults report using Facebook",
        "source": "Pew Research Center, 2025",
        "url": "https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Facebook remains a key platform for digital advertising scale.", "strength": 0.9
    },
    {
        "fact": "50% of U.S. adults say they use Instagram",
        "source": "Pew Research Center, 2025",
        "url": "https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Instagram provides strong reach for visual and influencer marketing.", "strength": 0.9
    },
    {
        "fact": "37% of U.S. adults report using TikTok",
        "source": "Pew Research Center, 2025",
        "url": "https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/",
        "tag": "PRO", "domain": "marketing",
        "summary": "TikTok is rapidly growing as a short-form content marketing channel.", "strength": 0.9
    },
    {
        "fact": "96% of U.S. teens report using the internet daily",
        "source": "Pew Research Center, 2024",
        "url": "https://www.pewresearch.org/internet/2024/12/12/teens-social-media-and-technology-2024/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Near-universal teen internet usage offers strong digital targeting potential.", "strength": 0.8
    },
    {
        "fact": "78% of organizations used AI in at least one business function in 2024, up from 20% in 2017",
        "source": "McKinsey Global Survey on AI, 2025",
        "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI adoption has surged dramatically over the past decade.", "strength": 0.9
    },
    {
        "fact": "AI-driven personalization can increase revenue by 5% to 8%",
        "source": "McKinsey Personalization Research, 2025",
        "url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/agents-for-growth-turning-ai-promise-into-impact",
        "tag": "PRO", "domain": "finance",
        "summary": "Personalization directly contributes to revenue growth.", "strength": 0.9
    },
    {
        "fact": "AI-driven personalization can reduce costs by up to 30%",
        "source": "McKinsey Personalization Research, 2025",
        "url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/agents-for-growth-turning-ai-promise-into-impact",
        "tag": "PRO", "domain": "finance",
        "summary": "AI can significantly lower operational costs in marketing.", "strength": 0.9
    },
    {
        "fact": "AI-driven personalization can improve customer satisfaction by 15% to 20%",
        "source": "McKinsey Personalization Research, 2025",
        "url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/agents-for-growth-turning-ai-promise-into-impact",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI enhances customer experience through tailored interactions.", "strength": 0.9
    },
    {
        "fact": "Generative AI could add $4.4 trillion annually to global productivity",
        "source": "McKinsey Global Institute, 2025",
        "url": "https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work",
        "tag": "PRO", "domain": "finance",
        "summary": "AI has massive macroeconomic growth potential.", "strength": 0.9
    },
    {
        "fact": "More than 80% of organizations report no organization-wide profit impact from AI yet",
        "source": "McKinsey AI Analysis, 2025",
        "url": "https://www.aicerts.ai/news/mckinsey-signals-inflection-in-ai-value-capture/",
        "tag": "CON", "domain": "finance",
        "summary": "Despite adoption, many firms struggle to realize AI profits.", "strength": 0.9
    },
    {
        "fact": "87% of companies expect AI to increase revenue within three years",
        "source": "McKinsey AI Analysis, 2025",
        "url": "https://www.aicerts.ai/news/mckinsey-signals-inflection-in-ai-value-capture/",
        "tag": "PRO", "domain": "finance",
        "summary": "Businesses are optimistic about AI-driven growth.", "strength": 0.9
    },
    {
        "fact": "50% of consumers currently use AI-powered search tools",
        "source": "McKinsey Digital Consumer Insights, 2025",
        "url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/new-front-door-to-the-internet-winning-in-the-age-of-ai-search",
        "tag": "PRO", "domain": "marketing",
        "summary": "AI is reshaping how consumers search and discover products.", "strength": 0.9
    },
    {
        "fact": "AI-powered search could influence $750 billion in consumer spending by 2028",
        "source": "McKinsey Digital Consumer Insights, 2025",
        "url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/new-front-door-to-the-internet-winning-in-the-age-of-ai-search",
        "tag": "PRO", "domain": "finance",
        "summary": "AI search is expected to significantly impact global commerce.", "strength": 0.9
    },


    # ── New Finance Facts (UNCTAD / Atlantic Council / S&P / ILO / Chainalysis) ──
    {
        "fact": "Global trade in goods and services reached approximately $33 trillion in 2024, with goods accounting for $25 trillion and services $8 trillion.",
        "source": "UNCTAD Key Statistics and Trends in International Trade, 2024",
        "url": "https://unctad.org/publication/key-statistics-and-trends-international-trade-2024",
        "tag": "PRO", "domain": "finance",
        "summary": "Global trade hit a new record in 2024, demonstrating the resilience of international commerce.", "strength": 0.85
    },
    {
        "fact": "Global merchandise exports fell 4.3% to $23.8 trillion in 2023, with developing economies declining more steeply at -6.2%.",
        "source": "UNCTAD Handbook of Statistics, 2024",
        "url": "https://unctad.org/publication/handbook-statistics-2024",
        "tag": "CON", "domain": "finance",
        "summary": "Merchandise trade contraction disproportionately hurt developing economies in 2023.", "strength": 0.85
    },
    {
        "fact": "Global services exports rose 8.3% to $7.9 trillion in 2023, led by travel (34%) and digitally deliverable services (over 8%).",
        "source": "UNCTAD Handbook of Statistics, 2024",
        "url": "https://unctad.org/publication/handbook-statistics-2024",
        "tag": "PRO", "domain": "finance",
        "summary": "Services trade surged in 2023, driven by digital delivery and travel recovery.", "strength": 0.85
    },
    {
        "fact": "Developing countries paid $50 billion more to external creditors than they received in new loans in 2022, worsening their debt crisis.",
        "source": "UNCTAD Trade and Development Report Update, April 2024",
        "url": "https://unctad.org/publication/trade-and-development-report-update-april-2024",
        "tag": "CON", "domain": "finance",
        "summary": "Developing nations face unsustainable debt outflows that undermine investment and growth.", "strength": 0.9
    },
    {
        "fact": "By 2023, nine low-income countries had fallen into debt distress, with an additional 25 on the brink, according to UNCTAD.",
        "source": "UNCTAD Trade and Development Report Update, April 2024",
        "url": "https://unctad.org/publication/trade-and-development-report-update-april-2024",
        "tag": "CON", "domain": "finance",
        "summary": "A growing wave of sovereign debt crises threatens the developing world.", "strength": 0.9
    },
    {
        "fact": "The global economy is projected to grow at just 2.7% for 2024 and 2025, a 'low normal' far below the 4.4% pre-financial-crisis average.",
        "source": "UNCTAD Trade and Development Report 2024",
        "url": "https://unctad.org/publication/trade-and-development-report-2024",
        "tag": "CON", "domain": "finance",
        "summary": "Structural economic slowdown has become entrenched, not cyclical.", "strength": 0.9
    },
    {
        "fact": "Developing economies' average growth fell to 4.1% in 2014–2024, sharply down from 6.6% during 2003–2013.",
        "source": "UNCTAD Trade and Development Report 2024",
        "url": "https://unctad.org/publication/trade-and-development-report-2024",
        "tag": "CON", "domain": "finance",
        "summary": "The developing world's growth engine has weakened significantly over the past decade.", "strength": 0.85
    },
    {
        "fact": "More than half of world trade now takes place between countries party to a preferential trade agreement, up from a minority in the early 2000s.",
        "source": "UNCTAD Key Statistics and Trends in Trade Policy, 2024",
        "url": "https://unctad.org/publication/key-statistics-and-trends-trade-policy-2024",
        "tag": "PRO", "domain": "finance",
        "summary": "Regional trade integration has reshaped the architecture of global commerce.", "strength": 0.8
    },
    {
        "fact": "China's digital yuan (e-CNY) reached 7 trillion yuan ($986 billion) in total transaction volume across 17 provinces by June 2024, nearly four times the 2023 level.",
        "source": "Atlantic Council CBDC Tracker, 2025",
        "url": "https://www.atlanticcouncil.org/cbdctracker/",
        "tag": "PRO", "domain": "finance",
        "summary": "China's CBDC pilot has achieved near-trillion-dollar transaction scale, the world's largest.", "strength": 0.9
    },
    {
        "fact": "137 countries and currency unions representing 98% of global GDP are now exploring a CBDC, up from just 35 countries in May 2020.",
        "source": "Atlantic Council CBDC Tracker, 2025",
        "url": "https://www.atlanticcouncil.org/cbdctracker/",
        "tag": "PRO", "domain": "finance",
        "summary": "CBDC exploration has become near-universal among major economies within five years.", "strength": 0.9
    },
    {
        "fact": "A record 49 CBDC pilot projects are now underway globally, with 3 countries — the Bahamas, Jamaica, and Nigeria — having fully launched digital currencies.",
        "source": "Atlantic Council CBDC Tracker, 2025",
        "url": "https://www.atlanticcouncil.org/cbdctracker/",
        "tag": "PRO", "domain": "finance",
        "summary": "Digital currency pilots have reached a critical mass, with full launches already operational.", "strength": 0.85
    },
    {
        "fact": "India's digital rupee circulation rose 334% to $122 million by March 2025, making it the world's second-largest CBDC pilot after China.",
        "source": "Atlantic Council CBDC Tracker, 2025",
        "url": "https://www.atlanticcouncil.org/cbdctracker/",
        "tag": "PRO", "domain": "finance",
        "summary": "India's CBDC adoption is accelerating at triple-digit rates, validating digital currency viability.", "strength": 0.85
    },
    {
        "fact": "In 2025, President Trump issued an executive order to halt all work on a US retail CBDC, making the US the only major economy to formally reverse course.",
        "source": "Atlantic Council CBDC Tracker, 2025",
        "url": "https://www.atlanticcouncil.org/cbdctracker/",
        "tag": "CON", "domain": "finance",
        "summary": "US political opposition to CBDC creates a major gap in global digital finance coordination.", "strength": 0.85
    },
    {
        "fact": "Of all global corporate defaults tracked since 1981, 72% were rated below CCC+ at the time of default; investment-grade defaults account for just 0.5%.",
        "source": "S&P Global Ratings, 2024 Annual Global Corporate Default Study",
        "url": "https://www.spglobal.com/ratings/en/research-insights/research/default-transition-and-recovery",
        "tag": "PRO", "domain": "finance",
        "summary": "Credit ratings are strong predictors of default risk — investment-grade bonds are highly safe.", "strength": 0.9
    },
    {
        "fact": "In 2024, the global corporate credit upgrade rate rose to 8.6% from 6.7%, while the downgrade rate fell to 6.7% from 9.3%, signalling improving credit quality.",
        "source": "S&P Global Ratings, 2024 Annual US Corporate Default Study",
        "url": "https://www.spglobal.com/ratings/en/research-insights/research/default-transition-and-recovery",
        "tag": "PRO", "domain": "finance",
        "summary": "Credit quality improved in 2024 despite economic headwinds, with upgrades outpacing downgrades.", "strength": 0.85
    },
    {
        "fact": "S&P Global projects the global speculative-grade corporate default rate will rise to 3.75% by March 2026, signalling elevated credit stress ahead.",
        "source": "S&P Global Ratings Default, Transition and Recovery Report, 2025",
        "url": "https://www.spglobal.com/ratings/en/research-insights/research/default-transition-and-recovery",
        "tag": "CON", "domain": "finance",
        "summary": "Rising speculative-grade defaults signal growing financial stress in leveraged credit markets.", "strength": 0.85
    },
    {
        "fact": "Global unemployment was 4.9% in 2024, with a jobs gap of 402 million people worldwide who wanted work but could not find it.",
        "source": "ILO World Employment and Social Outlook, May 2024 Update",
        "url": "https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-may-2024-update",
        "tag": "CON", "domain": "finance",
        "summary": "The global jobs gap dwarfs headline unemployment figures, revealing the true scale of labour underutilisation.", "strength": 0.9
    },
    {
        "fact": "Workers in informal employment crossed 2 billion in 2023, representing 58% of the global workforce — a structural barrier to economic development.",
        "source": "ILO World Employment and Social Outlook: Trends 2024",
        "url": "https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-trends-2024",
        "tag": "CON", "domain": "finance",
        "summary": "The majority of the world's workers lack formal contracts, legal protections, or social security.", "strength": 0.9
    },
    {
        "fact": "77% of employers globally are challenged to find workers with the right skill set, compared to only 35% a decade ago.",
        "source": "ILO World Employment and Social Outlook: Trends 2024",
        "url": "https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-trends-2024",
        "tag": "CON", "domain": "finance",
        "summary": "A worsening global skills gap is constraining labour markets and economic productivity.", "strength": 0.85
    },
    {
        "fact": "Real wages declined in the majority of G20 countries in 2023 as inflation outpaced wage growth, eroding purchasing power.",
        "source": "ILO World Employment and Social Outlook: Trends 2024",
        "url": "https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-trends-2024",
        "tag": "CON", "domain": "finance",
        "summary": "Inflation-driven real wage declines have eroded living standards across the world's largest economies.", "strength": 0.85
    },
    {
        "fact": "Illicit cryptocurrency addresses received $40.9 billion in 2024, a figure projected to exceed $51 billion once all illicit addresses are identified.",
        "source": "Chainalysis Crypto Crime Report, 2025",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "Crypto-enabled financial crime has reached multi-billion dollar scale, undermining regulatory trust.", "strength": 0.9
    },
    {
        "fact": "Stablecoins now account for 63% of all illicit cryptocurrency transaction volume in 2024, overtaking Bitcoin as the preferred asset for cybercriminals.",
        "source": "Chainalysis Crypto Crime Report, 2025",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "The stability of stablecoins paradoxically makes them the dominant vehicle for crypto crime.", "strength": 0.9
    },
    {
        "fact": "North Korean hackers stole $1.34 billion in cryptocurrency in 2024, accounting for 61% of all crypto stolen funds globally.",
        "source": "Chainalysis Crypto Crime Report, 2025",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "State-sponsored crypto theft has become a billion-dollar national security threat.", "strength": 0.9
    },
    {
        "fact": "In 2025, illicit cryptocurrency addresses received $154 billion — a 162% year-over-year increase driven largely by sanctioned state actors.",
        "source": "Chainalysis Crypto Crime Report, 2026",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "Crypto crime has reached an unprecedented scale as nation-states weaponise blockchain finance.", "strength": 0.95
    },
    {
        "fact": "Despite record illicit volumes, the illicit share of all cryptocurrency transactions remains below 1%, showing that most crypto activity is legitimate.",
        "source": "Chainalysis Crypto Crime Report, 2026",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "PRO", "domain": "finance",
        "summary": "Crypto crime, while large in absolute terms, is a tiny fraction of the total blockchain economy.", "strength": 0.85
    },
    {
        "fact": "Huione Guarantee, a criminal marketplace, has processed over $70 billion in crypto transactions since 2021, illustrating the professionalisation of crypto crime.",
        "source": "Chainalysis Crypto Crime Report, 2025",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "Organised crime has built industrial-scale infrastructure to launder and move illicit crypto.", "strength": 0.9
    },
    {
        "fact": "Total cryptocurrency stolen via hacks rose 21% year-over-year to $2.2 billion in 2024, with private key compromises accounting for 43.8% of thefts.",
        "source": "Chainalysis Crypto Crime Report, 2025",
        "url": "https://www.chainalysis.com/reports/",
        "tag": "CON", "domain": "finance",
        "summary": "Crypto theft is accelerating, with key management failures as the single largest attack vector.", "strength": 0.9
    },
    {
        "fact": "Global FDI fell 2% to $1.33 trillion in 2023, with developing economies experiencing a sharper 7% decline, reducing capital available for development.",
        "source": "UNCTAD Handbook of Statistics, 2024",
        "url": "https://unctad.org/publication/handbook-statistics-2024",
        "tag": "CON", "domain": "finance",
        "summary": "Falling FDI disproportionately deprives developing nations of the investment they most need.", "strength": 0.85
    },


    # ── New Marketing Facts (Genesys, DataReportal, Capital One Shopping) ──────
    {
        "fact": "Content marketing costs 62% less than traditional marketing while generating 3x more leads.",
        "source": "Genesys Growth / Clearscope, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "PRO", "domain": "marketing",
        "summary": "Content marketing's cost advantage over traditional channels is decisive.", "strength": 0.9
    },
    {
        "fact": "Content marketing generates $3 for every $1 invested, compared to $1.80 for paid advertising — a 67% performance advantage.",
        "source": "Genesys Growth / Revenue Zen, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "PRO", "domain": "marketing",
        "summary": "Content marketing delivers nearly double the ROI of paid advertising.", "strength": 0.9
    },
    {
        "fact": "SEO delivers 748% ROI for B2B companies — the highest-returning digital marketing channel available.",
        "source": "Genesys Growth / Data Mania, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "PRO", "domain": "marketing",
        "summary": "B2B SEO produces extraordinary returns that dwarf other digital marketing investments.", "strength": 0.95
    },
    {
        "fact": "Companies blogging consistently see 13x more positive ROI than sporadic publishers.",
        "source": "Genesys Growth / Firework, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "PRO", "domain": "marketing",
        "summary": "Content marketing consistency produces outsized compounding returns.", "strength": 0.9
    },
    {
        "fact": "Only 36% of marketing leaders can accurately measure content ROI, despite 83% prioritising its demonstration — a critical accountability gap.",
        "source": "Genesys Growth / Clearscope, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "CON", "domain": "marketing",
        "summary": "Most marketing organisations cannot prove the value of their content investment.", "strength": 0.9
    },
    {
        "fact": "Video delivers ROI 49% faster than text-based content, making it critical for organisations needing quicker investment returns.",
        "source": "Genesys Growth, 2026",
        "url": "https://genesysgrowth.com/blog/content-marketing-roi-stats-for-marketing-leaders",
        "tag": "PRO", "domain": "marketing",
        "summary": "Video content compresses the ROI timeline significantly compared to written formats.", "strength": 0.85
    },
    {
        "fact": "Global advertising spend reached approximately $1.1 trillion in 2024, a 7.3% increase year-on-year, and has grown over 50% since 2019.",
        "source": "DataReportal Digital 2025 / Statista Market Insights",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "The global advertising market hit a trillion-dollar milestone, reflecting sustained investment in brand communication.", "strength": 0.95
    },
    {
        "fact": "Digital channels now account for 72.7% of worldwide ad investment, exceeding $790 billion in 2024 — up from just under 50% in 2018.",
        "source": "DataReportal Digital 2025 / Statista",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "Digital advertising's dominance of global ad spend has become structural and irreversible.", "strength": 0.95
    },
    {
        "fact": "Mobile accounted for 65.3% of all digital advertising spend in 2024, up from 52.7% in 2019 — a structural shift toward mobile-first marketing.",
        "source": "DataReportal Digital 2025 / Statista",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "Mobile has become the dominant device for digital advertising, reshaping all marketing strategies.", "strength": 0.9
    },
    {
        "fact": "Programmatic advertising accounted for 82.4% of digital ad spend in 2024, with businesses spending over $650 billion on programmatic placements.",
        "source": "DataReportal Digital 2025 / Statista",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "Programmatic automation now dominates digital advertising, reshaping how media is bought and sold.", "strength": 0.9
    },
    {
        "fact": "73% of internet users still regularly discover new brands through traditional media — TV, print, and radio — despite digital ad spend growth.",
        "source": "DataReportal Digital 2025 / GWI",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "NEUTRAL", "domain": "marketing",
        "summary": "Traditional media retains significant brand discovery power even as budgets shift digital.", "strength": 0.85
    },
    {
        "fact": "US ad spend per capita reached $1,246 per person in 2024 — the highest in the world — reflecting the country's outsized marketing investment.",
        "source": "DataReportal Digital 2025 / Statista",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "The US leads the world in advertising intensity, underscoring the scale of the marketing economy.", "strength": 0.85
    },
    {
        "fact": "Search platforms earned over $316 billion in digital ad revenue in 2024 — 40% of all digital spend — growing 12% year-on-year.",
        "source": "DataReportal Digital 2025 / Statista",
        "url": "https://datareportal.com/reports/digital-2025-sub-section-global-advertising-trends",
        "tag": "PRO", "domain": "marketing",
        "summary": "Search advertising remains the single largest digital channel, driven by purchase-intent traffic.", "strength": 0.9
    },
    {
        "fact": "65% of all business revenue comes from repeat customers, who spend 67% more per transaction than new customers.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Loyal customers are dramatically more valuable than new customers on every financial metric.", "strength": 0.95
    },
    {
        "fact": "A 5% increase in customer loyalty increases profits by 25%–95%, making retention the highest-ROI lever in marketing.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Marginal improvements in customer retention produce outsized profit gains.", "strength": 0.95
    },
    {
        "fact": "74% of consumers globally claim brand loyalty, and 80% of Americans are loyal to at least one brand.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Brand loyalty is a near-universal consumer behaviour that represents an enormous strategic asset.", "strength": 0.9
    },
    {
        "fact": "75% of global consumers say they would switch brands for a loyalty programme with better rewards.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "CON", "domain": "marketing",
        "summary": "Brand loyalty is highly contingent on programme value — most consumers are not unconditionally loyal.", "strength": 0.9
    },
    {
        "fact": "29% of US consumers deliberately stopped using a brand in a 12-month period due to a single bad customer experience.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "CON", "domain": "marketing",
        "summary": "Brand loyalty is fragile — a single poor experience can permanently lose nearly a third of customers.", "strength": 0.9
    },
    {
        "fact": "89% of US consumers favour brands that share their values, and 54% remain loyal specifically because a brand takes a public stance on social issues.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "PRO", "domain": "marketing",
        "summary": "Brand values alignment is a primary loyalty driver — purpose-driven marketing creates durable customer bonds.", "strength": 0.9
    },
    {
        "fact": "Brand-loyal customers are worth 2.5x more revenue than new customers, and over 10 years boost shareholder returns between 2 and 5 times.",
        "source": "Capital One Shopping Research, Brand Loyalty Statistics, 2025",
        "url": "https://capitaloneshopping.com/research/brand-loyalty-statistics/",
        "tag": "PRO", "domain": "marketing",
        "summary": "The long-term financial compounding effect of brand loyalty is transformative for shareholder value.", "strength": 0.95
    },

    {
        "fact": "AI systems have demonstrated the ability to generate functional bioweapon synthesis routes, leading biosecurity experts to call for emergency governance measures.",
        "source": "Future of Life Institute / RAND Corporation biosecurity analysis, 2025",
        "url": "https://futureoflife.org/focus-area/artificial-intelligence/",
        "tag": "CON", "domain": "ethics",
        "summary": "Frontier AI's potential for enabling mass-casualty bioweapons represents an existential governance failure.", "strength": 0.95
    },
    {
        "fact": "Over 1,000 AI researchers signed an open letter warning that AI systems trained without adequate alignment techniques may pursue goals harmful to humanity.",
        "source": "Center for AI Safety (safe.ai), 2024",
        "url": "https://safe.ai/research",
        "tag": "CON", "domain": "ethics",
        "summary": "The AI research community itself has publicly flagged catastrophic risk from misaligned AI systems.", "strength": 0.9
    },

    # ══════════════════════════════════════════════════════
    # GENERAL (fallback for unknown topics)
    # ══════════════════════════════════════════════════════

    {
        "fact": "As of 2024, approximately 5.4 billion people use the internet, representing 67% of the global population.",
        "source": "DataReportal Global Digital Overview, 2024",
        "url": "https://datareportal.com/global-digital-overview",
        "tag": "NEUTRAL", "domain": "general",
        "summary": "Digital connectivity now reaches two-thirds of humanity.", "strength": 0.7
    },
    {
        "fact": "The global AI market is projected to reach $1.8 trillion by 2030.",
        "source": "Grand View Research, 2023",
        "url": "https://grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market",
        "tag": "PRO", "domain": "general",
        "summary": "AI represents one of the largest economic opportunities in history.", "strength": 0.8
    },
    {
        "fact": "Climate change costs the global economy an estimated $16 million per hour in extreme weather damages.",
        "source": "Deloitte Economics Institute, 2023",
        "url": "https://deloitte.com/global/en/issues/climate/the-turning-point.html",
        "tag": "CON", "domain": "general",
        "summary": "Climate inaction carries an enormous and accelerating economic price tag.", "strength": 0.85
    },
]


# ── Domain Detection ───────────────────────────────────────────────────────────

AVAILABLE_DOMAINS = ["finance", "marketing", "ethics", "general"]

# Cache: topic string -> list of matched domains (Groq called once per match)
_domain_cache: dict[str, list[str]] = {}

# Keyword fallback (used if Groq fails)
_DOMAIN_KEYWORDS = {
    "finance": [
        "finance", "financial", "economy", "economic", "gdp",
        "investment", "market", "banking", "debt", "inflation",
        "trade", "fiscal", "monetary", "stock", "crypto",
        "bank", "currency", "fund", "capital", "wealth"
    ],
    "marketing": [
        "marketing", "advertis", "brand", "consumer", "digital",
        "social media", "campaign", "customer", "sales", "content",
        "seo", "influencer", "ecommerce", "retail", "promotion",
        "audience", "engagement", "roi", "conversion"
    ],
    "ethics": [
        "ethics", "ethical", "ai", "artificial intelligence", "moral",
        "regulation", "bias", "fairness", "privacy", "responsible",
        "governance", "policy", "rights", "surveillance", "automation",
        "justice", "equality", "accountability", "transparency"
    ]
}


def detect_domains_groq(topic: str) -> list[str]:
    """
    Uses Groq to identify ALL relevant domains for a debate topic.
    Returns e.g. ["finance", "ethics"] for cross-domain topics.
    Cached — Groq called once per unique topic, zero per-turn cost after that.
    Falls back to keyword scoring if Groq fails.
    """
    if topic in _domain_cache:
        print(f"[facts] domain cache hit: {_domain_cache[topic]}")
        return _domain_cache[topic]

    try:
        import os
        from groq import Groq as _Groq
        _groq = _Groq(api_key=os.getenv("GROQ_API_KEY2", ""))

        prompt = (
            f"Available domains: {AVAILABLE_DOMAINS}\n"
            f"Debate topic: \"{topic}\"\n\n"
            "Choose ALL domains relevant to this topic. "
            "Reply with ONLY a comma-separated list, e.g.: finance,ethics\n"
            "Reply:"
        )

        resp    = _groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You classify debate topics into domains. Reply with comma-separated domain names only. No explanation."},
                {"role": "user",   "content": prompt}
            ],
            max_completion_tokens=20,
            temperature=0.0
        )
        raw     = resp.choices[0].message.content.strip().lower()
        domains = [d.strip() for d in raw.split(",") if d.strip() in AVAILABLE_DOMAINS]
        if not domains:
            domains = ["general"]
        _domain_cache[topic] = domains
        print(f"[facts] Groq domain detection: {domains}")
        return domains

    except Exception as e:
        print(f"[facts] Groq domain detection failed ({str(e)[:80]}) — keyword fallback")

    # Keyword fallback
    topic_lower = topic.lower()
    scores  = {d: sum(1 for kw in kws if kw in topic_lower) for d, kws in _DOMAIN_KEYWORDS.items()}
    matched = [d for d, s in scores.items() if s > 0]
    result  = matched if matched else ["general"]
    _domain_cache[topic] = result
    print(f"[facts] keyword fallback domains: {result}")
    return result


def get_facts_by_stance(topic: str, stance: str, max_facts: int = 4) -> list[dict]:
    """
    Returns top N facts filtered by ALL relevant domains + stance.
    Multi-domain aware — cross-domain topics get facts from all matching domains.
    Sorted by strength descending.
    """
    domains   = detect_domains_groq(topic)
    stance_up = stance.upper()

    # Pull from ALL matched domains
    pool = [f for f in FACTS if f["domain"] in domains]
    if not pool:
        pool = [f for f in FACTS if f["domain"] == "general"]

    # Filter by stance
    filtered = [f for f in pool if f["tag"] in (stance_up, "NEUTRAL")]

    # Sort by strength
    filtered.sort(key=lambda x: x.get("strength", 0.5), reverse=True)

    print(f"[facts] domains={domains} | stance={stance_up} | pool={len(pool)} | matched={len(filtered)}")
    return filtered[:max_facts]


def format_facts_for_prompt(facts: list[dict]) -> str:
    """
    Formats facts for injection into system prompt.
    Includes source and URL for credibility.
    """
    if not facts:
        return "No domain-specific facts available. Argue from logic and principle only."

    lines = ["VERIFIED FACTS — use these, never invent statistics:"]
    for f in facts:
        url_part = f" | {f['url']}" if f.get("url") else ""
        lines.append(f'• "{f["fact"]}" [{f["source"]}{url_part}]')

    return "\n".join(lines)


# ── Quick Self Test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # tests = [
    #     ("Cryptocurrency should replace traditional banking", "PRO"),
    #     ("Influencer marketing is more effective than traditional advertising", "CON"),
    #     ("AI companies should be held legally responsible for algorithmic bias", "PRO"),
    #     ("ESG investing is the future of finance", "CON"),
    #     ("Data privacy regulations hurt business innovation", "CON"),
    # ]

    # print("=" * 60)
    # print("FACTS.PY SELF TEST")
    # print("=" * 60)

    # for topic, stance in tests:
    #     facts  = get_facts_by_stance(topic, stance)
    #     output = format_facts_for_prompt(facts)
    #     print(f"\nTopic:  {topic}")
    #     print(f"Stance: {stance}")
    #     print(output)
    #     print("-" * 40)
    from facts import get_facts_by_stance, format_facts_for_prompt

    facts = get_facts_by_stance("Companies should be held legally liable for algorithmic bias", "PRO", 4)
    print(format_facts_for_prompt(facts))