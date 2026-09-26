import streamlit as st
def show_tips():
 
    st.markdown("""
        <style>
        .stApp { background-color: #030508; color: white; }
        
        /* Main Neon Border Box */
        .neon-outer-box { border: 2px solid #00d4ff;  border-radius: 20px;
            padding: 30px; background: rgba(0, 212, 255, 0.02);
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.3), inset 0 0 15px rgba(0, 212, 255, 0.05);
            margin-top: 15px;
        }

        .neon-title {
            color: #00d4ff; font-size: 3rem; font-weight: 800; text-align: center; text-transform: uppercase; letter-spacing: 4px;
            text-shadow: 0 0 15px #00d4ff, 0 0 30px rgba(0, 212, 255, 0.5); margin-bottom: 5px;
        }

        /* Floating Animation for Cards */
        @keyframes floatUp {
            0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); }
        }

        .strategy-card {
            background: rgba(255, 255, 255, 0.03);  border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 12px;  padding: 18px; margin-bottom: 15px;display: flex;align-items: flex-start;  transition: 0.4s ease; animation: floatUp 0.6s ease forwards;
        }

        .strategy-card:hover {
            border-color: #00d4ff;box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);transform: translateY(-5px);  background: rgba(0, 212, 255, 0.08);
        }

        .step-num {
            color: #00d4ff; font-weight: 900; font-size: 1.4rem;margin-right: 15px; text-shadow: 0 0 8px #00d4ff;
        }

        .step-text { color: #eee; font-size: 0.95rem; line-height: 1.5; }

        /* Custom Dropdown */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #0a0f1a !important;
            border: 1px solid #00d4ff !important;
            border-radius: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('''
<style>
@keyframes underlineSlide { 0% { transform: translateX(-100%); } 50% { transform: translateX(100%); } 100% { transform: translateX(100%); } }
@keyframes iconGlow { 0%,100% { box-shadow:0 0 12px rgba(0,212,255,0.3); } 50% { box-shadow:0 0 20px rgba(0,212,255,0.6); } }
</style>
<div style="text-align:left; padding:22px 28px; margin-bottom:20px;background: rgba(0, 212, 255, 0.15); border:2px solid #00d4ff; border-radius:16px; position:relative; overflow:hidden; box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);">
<div style="display:flex; align-items:flex-start; gap:18px;">
<div style="width:56px; height:56px; border-radius:50%; background:radial-gradient(circle, rgba(0,212,255,0.18), rgba(0,212,255,0.02));
border:1.5px solid rgba(0,212,255,0.4); display:flex; align-items:center; justify-content:center; flex-shrink:0;
animation:iconGlow 2.5s ease-in-out infinite;">
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/compass.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Orbitron',sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">CAREER ROADMAPS</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Curated, <span style="color:#00d4ff; font-weight:700;">role-specific</span> roadmaps &mdash;
<span style="color:#00d4ff; font-weight:700;">researched and structured</span>, not AI-generated.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)

    # --- 10 ROLES WITH 12 DETAILED TIPS EACH ---
    ROLES_DATA = {
        "Software Development Engineer (SDE)": [
            "Master Data Structures & Algorithms (Focus on Graphs, DP, and Trees).",
            "Solve at least 400+ curated problems on LeetCode (Medium/Hard level).",
            "Build 2 scalable Full-Stack projects using MERN or Python/Django.",
            "Understand Low-Level Design (LLD) using Design Patterns (Singleton, Factory).",
            "Learn High-Level Design (HLD) concepts like Sharding, Caching, and Load Balancing.",
            "Master SQL and NoSQL databases (Optimization and Indexing).",
            "Deep dive into Computer Science fundamentals (OS, DBMS, Computer Networks).",
            "Contribute to Open Source and maintain a professional GitHub profile.",
            "Learn DevOps basics: Docker, Kubernetes, and CI/CD pipelines.",
            "Master Version Control (Git) and collaborative workflows like Gitflow.",
            "Prepare for behavioral rounds using the STAR method for leadership questions.",
            "Network with engineers at target companies via LinkedIn for referrals."
        ],
        "Data Scientist": [
            "Master Python/R libraries: Pandas, NumPy, Scikit-Learn, and Matplotlib.",
            "Strengthen Mathematics: Linear Algebra, Calculus, and Inferential Statistics.",
            "Learn Exploratory Data Analysis (EDA) to find hidden patterns in raw data.",
            "Master SQL for complex data extraction and joins from warehouses.",
            "Understand Machine Learning algorithms (Regression, Trees, SVM, Clustering).",
            "Learn Deep Learning frameworks like TensorFlow or PyTorch for AI tasks.",
            "Master Data Visualization tools like Tableau or PowerBI for storytelling.",
            "Understand Feature Engineering and handling imbalanced datasets.",
            "Learn Big Data technologies like Apache Spark or Hadoop for large scales.",
            "Master Model Deployment using Flask, FastAPI, or AWS SageMaker.",
            "Practice on Kaggle to learn from global data science competitions.",
            "Develop business acumen to translate data into actionable insights."
        ],
        "Cybersecurity Analyst": [
            "Master Networking protocols (TCP/IP, DNS, HTTP/S, SSH).",
            "Learn Linux System Administration and Bash/Python scripting.",
            "Understand the OWASP Top 10 vulnerabilities (XSS, SQLi, CSRF).",
            "Practice Penetration Testing on TryHackMe or HackTheBox platforms.",
            "Learn SIEM tools like Splunk or ELK for security monitoring.",
            "Master Cryptography: Symmetric/Asymmetric encryption and Hashing.",
            "Understand Cloud Security specifically for AWS, Azure, or GCP.",
            "Get industry certifications: CompTIA Security+, CEH, or CISSP.",
            "Learn Incident Response and Digital Forensics (DFIR) procedures.",
            "Study Identity and Access Management (IAM) and Zero Trust models.",
            "Understand Firewalls, IDS/IPS, and Endpoint Detection (EDR).",
            "Stay updated with daily CVEs and global threat intelligence reports."
        ],
        "AI/ML Engineer": [
            "Deep dive into Neural Network architectures (CNN, RNN, Transformers).",
            "Master Computer Vision (OpenCV) or Natural Language Processing (NLP).",
            "Learn Model Optimization (Quantization, Pruning) for edge devices.",
            "Master MLOps tools like MLflow, DVC, and Kubeflow for pipelines.",
            "Understand Reinforcement Learning and Generative AI (GANs, LLMs).",
            "Learn to clean and curate high-quality datasets for training.",
            "Master Data Pipelines and ETL processes for ML-ready data.",
            "Understand Model Drift and performance monitoring in production.",
            "Practice GPU programming and distributed training techniques.",
            "Build projects around RAG (Retrieval Augmented Generation) for LLMs.",
            "Read latest AI research papers on ArXiv to stay at the cutting edge.",
            "Learn to deploy scalable AI models using Docker and Cloud APIs."
        ],
        "DevOps Engineer": [
            "Master Linux (Ubuntu/CentOS) and Shell Scripting for automation.",
            "Learn Infrastructure as Code (IaC) using Terraform or Ansible.",
            "Master Docker Containerization and Kubernetes Orchestration.",
            "Build robust CI/CD pipelines using GitHub Actions or Jenkins.",
            "Master Cloud Services (AWS/GCP/Azure) specifically IAM and VPC.",
            "Learn Monitoring and Alerting using Prometheus and Grafana.",
            "Understand Logging strategies with ELK stack or Graylog.",
            "Learn Site Reliability Engineering (SRE) to ensure high availability.",
            "Master GitOps practices for automated infrastructure updates.",
            "Understand Network Security, SSL/TLS, and Load Balancing.",
            "Learn DevSecOps to integrate security into every build phase.",
            "Master Scripting in Python or Go for internal tool development."
        ],
        "Cloud Architect": [
            "Master AWS/Azure/GCP Cloud Design Patterns for scalability.",
            "Understand Serverless architectures like AWS Lambda or Google Functions.",
            "Learn Cloud Networking: VPCs, Subnets, Gateways, and Route Tables.",
            "Master Cloud Storage solutions (S3, EBS, Glacier, RDS).",
            "Understand Disaster Recovery and Backup strategies across regions.",
            "Learn Cost Optimization to manage cloud billing effectively.",
            "Master Identity Management and Cloud Compliance standards.",
            "Understand Hybrid Cloud and Multi-Cloud connectivity solutions.",
            "Learn to design Fault-Tolerant and Highly Available systems.",
            "Master Migration strategies from on-premise to Cloud.",
            "Stay certified (AWS Solutions Architect, Azure Expert, etc.).",
            "Understand API Management and Microservices communication."
        ],
        "Backend Developer": [
            "Master a Backend language like Node.js, Python, Java, or Go.",
            "Understand Relational (PostgreSQL) and NoSQL (MongoDB) databases.",
            "Learn to design robust RESTful and GraphQL APIs.",
            "Master Caching techniques using Redis or Memcached.",
            "Understand Microservices architecture and Message Queues (Kafka/RabbitMQ).",
            "Learn Server-side security and Authentication (JWT, OAuth2).",
            "Master Unit Testing and Integration Testing for backend logic.",
            "Understand Scaling: Vertical vs Horizontal and Database Sharding.",
            "Learn to write Clean, Maintainable, and Documented code.",
            "Master System Monitoring and Error Logging for servers.",
            "Understand Web Servers like Nginx and Apache configuration.",
            "Deep dive into Concurrency and Multithreading in your language."
        ],
        "Frontend Developer": [
            "Master HTML5, CSS3, and Modern JavaScript (ES6+).",
            "Learn CSS Architectures like SASS and frameworks like Tailwind.",
            "Master a Frontend library: React, Next.js, or Vue.js.",
            "Understand State Management (Redux, Zustand, or Context API).",
            "Learn Web Performance Optimization (Lazy Loading, Memoization).",
            "Master Responsive Design and Cross-browser compatibility.",
            "Learn Frontend Testing frameworks like Jest or Cypress.",
            "Understand Browser APIs and Document Object Model (DOM).",
            "Master Web Accessibility (A11Y) and SEO fundamentals.",
            "Learn UI/UX tools like Figma to bridge design and code.",
            "Understand Module Bundlers like Webpack, Vite, or Parcel.",
            "Master Version Control and agile frontend workflows."
        ],
        "Data Engineer": [
            "Master Big Data tools: Apache Spark, Hadoop, and Hive.",
            "Learn to design complex ETL/ELT pipelines for data flow.",
            "Master SQL for data warehousing (Snowflake, BigQuery).",
            "Learn NoSQL databases (Cassandra, HBase, DynamoDB).",
            "Master Data Orchestration using Apache Airflow or Prefect.",
            "Understand Data Modeling and Schema Design (Star/Snowflake).",
            "Learn Stream Processing using Kafka Streams or Flink.",
            "Understand Data Lakehouse architectures (Delta Lake, Iceberg).",
            "Master Python or Scala for heavy data processing tasks.",
            "Learn to ensure Data Quality and Governance across systems.",
            "Understand Cloud Data services on AWS (Glue, Redshift).",
            "Learn to optimize pipeline performance and reduce latency."
        ],
        "Blockchain Developer": [
            "Master Solidity for Ethereum Smart Contract development.",
            "Understand Blockchain fundamentals: Consensus, Nodes, and Hashes.",
            "Learn Web3.js or Ethers.js to connect frontend with blockchain.",
            "Master Smart Contract Security and common attack patterns (Reentrancy).",
            "Learn Decentralized Storage like IPFS or Filecoin.",
            "Understand DeFi (Decentralized Finance) and Tokenomics design.",
            "Master Layer 2 scaling solutions (Polygon, Arbitrum).",
            "Learn alternative ecosystems like Solana (Rust) or Polkadot.",
            "Understand DAO (Decentralized Autonomous Organization) structures.",
            "Learn to use Hardhat or Foundry for testing and deployment.",
            "Master Cryptography basics: ECDSA and Zero-Knowledge Proofs.",
            "Stay updated with EIPs (Ethereum Improvement Proposals)."
        ],
        "Full Stack Developer": [
            "Master both Frontend (React/Next.js) and Backend (Node.js/Python/Java).",
            "Learn database design using both SQL (PostgreSQL) and NoSQL (MongoDB).",
            "Master State Management tools like Redux Toolkit or Zustand.",
            "Understand API integration, building secure RESTful and GraphQL endpoints.",
            "Learn authentication protocols and session management using JWT and OAuth2.",
            "Master version control via Git and collaborative workflows on GitHub.",
            "Understand cloud hosting and deployment basics on platforms like AWS, Vercel, or Heroku.",
            "Learn containerization basics using Docker for consistent environment setups.",
            "Optimize web performance using techniques like code splitting and lazy loading.",
            "Build responsive layouts using modern styling libraries like Tailwind CSS.",
            "Practice writing comprehensive integration tests for both client and server code.",
            "Develop a solid understanding of application security practices like CORS and security headers."
        ],
        "UI/UX Designer": [
            "Master professional design interfaces and prototyping workflows inside Figma.",
            "Understand foundational design principles: Typography, Visual Hierarchy, and Color Theory.",
            "Learn User Research methods like interviewing, persona creation, and empathy mapping.",
            "Master Wireframing techniques to map out high-level application flows cleanly.",
            "Understand Design Systems and component reuse strategies for consistent products.",
            "Learn to build highly interactive, high-fidelity responsive prototypes.",
            "Understand Web Accessibility standards (WCAG) to ensure inclusive digital designs.",
            "Learn Usability Testing strategies to gather concrete feedback from real test users.",
            "Master micro-interactions and animations to make software interfaces feel fluid.",
            "Develop a strong operational knowledge of HTML and CSS to bridge design-to-development gaps.",
            "Understand Mobile-First design architectures for modern cross-platform software.",
            "Build a compelling portfolio highlighting case studies and end-to-end design thinking."
        ],
        "Java Developer": [
            "Master core Java concepts: Object-Oriented Programming, Multithreading, and Collections.",
            "Deep dive into Java 8+ features like Streams, Lambda expressions, and Optional API.",
            "Master the Spring Boot ecosystem for building production-ready enterprise applications.",
            "Learn Microservices design patterns and inter-service communication workflows.",
            "Understand Object-Relational Mapping (ORM) frameworks like Hibernate and Spring Data JPA.",
            "Master unit testing libraries like JUnit and mocking tools like Mockito.",
            "Learn enterprise database management, focusing on PostgreSQL, Oracle, or MySQL optimization.",
            "Understand build management automation tools, specifically Apache Maven or Gradle.",
            "Learn secure API design practices using Spring Security and JWT setups.",
            "Understand caching mechanics at scale using tools like Redis or Ehcache.",
            "Master enterprise message architectures using brokers like Apache Kafka or RabbitMQ.",
            "Learn memory management principles, Garbage Collection tuning, and profiling tools."
        ],
        "Python Developer": [
            "Master core Python syntax, multi-paradigm design, and advanced scripting automation.",
            "Learn standard backend web development frameworks, focusing on Django or FastAPI.",
            "Understand asynchronous programming paradigms using asyncio and concurrent execution.",
            "Master database interactions using Object-Relational Mappers like SQLAlchemy or Django ORM.",
            "Learn task queuing workflows for background worker processing using Celery and Redis.",
            "Understand testing frameworks like pytest for writing clean, automated test suites.",
            "Master clean formatting standards, virtual environments, and package management via poetry or pip.",
            "Learn to build and document robust RESTful and context-driven custom APIs.",
            "Understand container-driven application setups using Docker environments.",
            "Learn core data-manipulation structures using standard libraries like Pandas and NumPy.",
            "Understand production application logging, monitoring structures, and WSGI/ASGI server setups.",
            "Practice continuous deployment workflows using automated pipeline tooling."
        ],
        "ML Engineer": [
            "Master core machine learning concepts: regression, classification, clustering, and ensemble methods.",
            "Deep dive into deep learning frameworks, specifically PyTorch or TensorFlow.",
            "Understand data preprocessing workflows, feature engineering, and dimensionality reduction.",
            "Learn to evaluate models using precision, recall, F1-score, and ROC-AUC curves.",
            "Master natural language processing frameworks or computer vision toolkits like OpenCV.",
            "Learn model deployment methodologies utilizing clean interfaces via FastAPI or Flask wrappers.",
            "Understand machine learning pipeline tracking and experimentation setups using MLflow.",
            "Learn version control tracking workflows for high-volume raw datasets using DVC.",
            "Understand containerization mechanics for reproducible runtime systems utilizing Docker containers.",
            "Master model efficiency optimization patterns, focusing on basic quantization and pruning.",
            "Learn distributed system computational setups across cluster architectures or local GPUs.",
            "Understand model performance drift monitoring mechanics across production configurations."
        ],
        "QA Automation Engineer": [
            "Master core object-oriented programming concepts using Java, Python, or JavaScript.",
            "Learn automated web testing frameworks thoroughly, focusing on Selenium WebDriver or Playwright.",
            "Understand API automation validation testing structures using REST Assured or Postman schemas.",
            "Master specialized mobile application testing platforms using Appium integration setups.",
            "Learn fundamental software testing methodologies, tracking boundary conditions and regression setups.",
            "Understand modern automated integration pipeline systems using tools like Jenkins or GitHub Actions.",
            "Master page object model design patterns to write highly reusable, scalable automation code.",
            "Learn comprehensive database state validation testing utilizing standard relational SQL queries.",
            "Understand performance and load distribution testing dynamics utilizing tools like Apache JMeter.",
            "Master structured issue reporting workflows inside centralized agile trackers like Jira logs.",
            "Learn continuous behavior-driven development framework setups using Cucumber or Gherkin files.",
            "Practice unified team code control check-ins using Git repository branching architectures."
        ],
        "Product Manager": [
            "Master customer discovery workflows, transforming user pain points into precise feature specs.",
            "Understand metric tracking foundations, defining clear KPIs for measuring product launch health.",
            "Learn wireframing and interactive canvas layout designs utilizing applications like Figma.",
            "Master lifecycle priority organization techniques like MoSCoW or RICE framework configurations.",
            "Understand market validation research patterns, performing deep competitor landscape analysis.",
            "Learn technical agile process operational frameworks, managing backlogs and sprint milestones.",
            "Master cross-functional communication, aligning engineering, design, and business stakeholder teams.",
            "Understand customer journey behavior tracking instrumentation using platforms like Mixpanel.",
            "Learn to design data-driven usability experiments, optimizing loops using strict A/B testing models.",
            "Master long-term product vision layout tracking, creating clean multi-quarter strategic roadmaps.",
            "Understand standard software pricing structures, positioning models, and go-to-market strategies.",
            "Develop strong financial fundamentals to evaluate business cases and calculate product ROI."
        ],
        "Security Engineer": [
            "Master defensive application security design reviews and secure code audit review models.",
            "Understand vulnerability categorization frameworks, analyzing systemic risks using OWASP models.",
            "Learn identity verification operational setups, focusing on OAuth2 profiles and SAML bindings.",
            "Master cryptographic application implementation choices, using symmetric cipher keys and hashes.",
            "Understand core cloud tenant boundary configurations, securing virtual network setups on AWS.",
            "Learn automated vulnerability detection integration inserted directly within active build systems.",
            "Master continuous threat modeling exercises, analyzing logical software boundaries for attack vectors.",
            "Understand network data layer packet monitoring loops using standard tools like Wireshark.",
            "Learn incident containment strategy definitions and digital artifact data recovery procedures.",
            "Master infrastructure compliance policy verification checking across active running software nodes.",
            "Understand modern container infrastructure cluster insulation policies within Kubernetes environments.",
            "Track daily global CVE publication lists to apply mitigation updates across staging setups."
        ],
        "Data Analyst": [
            "Master rapid data profiling workflows utilizing processing toolkits like Pandas or NumPy.",
            "Understand advanced multi-source table join aggregation expressions within SQL warehouses.",
            "Learn production-grade metric storytelling layout assembly using Tableau or Power BI.",
            "Master data cleaning operations, resolving outlier values and fixing missing structural blocks.",
            "Understand fundamental statistical probability distributions, validating variations using hypothesis testing.",
            "Learn exploratory reporting habits, discovering underlying seasonal patterns from history files.",
            "Master automated operational check scripts built cleanly using native Python configurations.",
            "Understand executive dashboard delivery formats, tracking company health patterns over time.",
            "Learn cross-functional metric extraction workflows to support strategic engineering choices.",
            "Master data translation skills to present technical analytics clearly to non-technical leaders.",
            "Understand standard data schema designs, focusing on analytical structures and table indices.",
            "Practice query code performance optimization to speed up high-volume database views."
        ],
        "Android Developer": [
            "Master modern mobile software construction using Kotlin and standard object-oriented patterns.",
            "Understand modern reactive user interface rendering systems utilizing Jetpack Compose components.",
            "Learn local relational caching mechanisms inside mobile databases using Room persistence libraries.",
            "Master mobile network layer integration architectures using Retrofit asynchronous processing.",
            "Understand clean architectural system separation patterns, focusing on MVVM structure layouts.",
            "Learn application memory performance profiling, identifying resource leaks across device runtimes.",
            "Master custom interface element animation transitions, ensuring highly fluid component movements.",
            "Understand background thread scheduling models utilizing Kotlin Coroutines and Flow mechanics.",
            "Learn dependency injection architecture setups using modern frameworks like Hilt or Dagger.",
            "Master local modular testing structures using specialized mobile frameworks like Espresso.",
            "Understand Google Play Console deployment parameters, bundle builds, and release workflows.",
            "Practice screen configuration adaptivity handling, building fluid scales across variable displays."
        ],
        "Network Engineer": [
            "Master foundational network routing and switching protocols, focusing on OSPF, BGP, and EIGRP.",
            "Understand software-defined networking (SDN) principles and modern campus network network design.",
            "Learn to configure and troubleshoot enterprise hardware, specifically Cisco, Juniper, or Aruba setups.",
            "Master IP addressing schema configurations, including advanced IPv4/IPv6 subnetting and VLSM.",
            "Understand network security isolation mechanics, using firewalls, ACLs, and secure VPN tunnels.",
            "Learn network performance monitoring workflows using terminal diagnostic tools and packet analyzers.",
            "Master wireless architecture design constraints, managing radio frequencies and secure roaming protocols.",
            "Understand infrastructure automation options using Python frameworks like Netmiko or Ansible playbooks.",
            "Learn DNS, DHCP, and IPAM (IP Address Management) configuration across distributed enterprise systems.",
            "Master load balancing design setups, routing traffic efficiently across redundant server farms.",
            "Understand cloud connectivity network topologies, establishing secure AWS Direct Connect or ExpressRoute lines.",
            "Practice continuous log auditing to proactively catch network vulnerabilities and prevent downtime."
        ],
        "Solutions Architect": [
            "Master the art of translating complex business objectives into scalable, secure technical software architectures.",
            "Understand multi-tier cloud application design patterns, ensuring system high availability and fault tolerance.",
            "Learn to evaluate trade-offs between monolithic structures and modular microservices architectures.",
            "Master data strategy design choices, mapping application requirements to the right SQL or NoSQL stores.",
            "Understand enterprise security frameworks, implementing identity federation and encryption at rest and transit.",
            "Learn cost estimation methodologies to design highly resource-efficient tech infrastructure systems.",
            "Master disaster recovery topology planning, ensuring low RTO and RPO metrics across service regions.",
            "Understand API management principles, designing secure, rate-limited gateway communication layouts.",
            "Learn to lead cross-functional technical teams, bridging gaps between developers and executive stakeholders.",
            "Master migration strategy frameworks, transitioning legacy local computing frameworks to the cloud.",
            "Understand compliance framework guidelines, aligning system designs with HIPAA, GDPR, or PCI-DSS rules.",
            "Practice continuous architecture reviews to refactor outdated subsystems and eliminate technical debt."
        ],
        "IT Support Engineer": [
            "Master hardware diagnostic routines, troubleshooting enterprise desktop, laptop, and mobile device issues.",
            "Understand multi-platform operating system configuration management across Windows, macOS, and Linux.",
            "Learn centralized user identity management structures, managing permissions inside Active Directory or Okta.",
            "Master network troubleshooting mechanics, resolving local connectivity, DNS, and VPN access problems.",
            "Understand enterprise software deployment methodologies, handling remote application patches securely.",
            "Learn ticket lifecycle tracking patterns, documenting resolution workflows inside platforms like Jira or ServiceNow.",
            "Master asset management protocols, auditing corporate hardware inventory lifecycle from procurement to disposal.",
            "Understand backup and data restoration operations, securing local user assets against file system corruption.",
            "Learn standard cybersecurity hygiene enforcement, isolating malware infections and handling phishing alerts.",
            "Master customer service communication practices, explaining technical concepts clearly to non-technical users.",
            "Understand remote support utility configurations, managing headless infrastructure nodes over secure tunnels.",
            "Practice writing comprehensive internal documentation and step-by-step user self-service knowledge base articles."
        ],
        "Database Administrator (DBA)": [
            "Master relational engine storage architectures, configuring instances for PostgreSQL, MySQL, or Oracle.",
            "Understand high availability database configurations, managing replication lag and automated failover groups.",
            "Learn advanced query tuning and optimization techniques, analyzing execution plans to fix slow transactions.",
            "Master transactional backup strategies, organizing point-in-time recovery setups to prevent data loss.",
            "Understand database security isolation models, managing granular user access controls and schema encryption.",
            "Learn system resource monitoring, tracking storage throughput, memory caching, and locking contentions.",
            "Master index management strategies, implementing B-Tree or Hash index updates without locking tables.",
            "Understand data migration frameworks, handling schema upgrades and data transformations across environments.",
            "Learn NoSQL cluster data administration, tracking shard key balancing inside MongoDB or Cassandra setups.",
            "Master automated maintenance script development, handling routine table vacuuming and statistics updates.",
            "Understand storage capacity planning methodologies, forecasting data growth to scale volume partitions.",
            "Practice routine log audit verification to track compliance metrics and catch unauthorized access patterns."
        ],
        "Site Reliability Engineer (SRE)": [
            "Master system reliability tracking indicators, defining precise Service Level Objectives (SLOs) and SLIs.",
            "Understand automated incident response workflows, minimizing time to resolution for production outages.",
            "Learn infrastructure performance profiling, tracking latency patterns across distributed microservices.",
            "Master chaos engineering experimentation models, testing cluster fault tolerance by injecting simulated failures.",
            "Understand advanced load shedding patterns and circuit breaker designs to prevent cascading system crashes.",
            "Learn to manage error budgets constructively, balancing rapid feature deployment with system stability limits.",
            "Master scalable telemetry architecture collection setups, organizing metric paths via OpenTelemetry pipelines.",
            "Understand container orchestration scale adjustments, tuning automated HPA profiles inside Kubernetes.",
            "Learn post-mortem root cause analysis habits, documenting structural logic faults to avoid repeat incidents.",
            "Master system architecture scaling configurations, optimizing caching boundaries to reduce database load.",
            "Understand declarative infrastructure deployment integrity validation checks within active build runners.",
            "Practice internal tooling automation scripting, eliminating operational toil using Python or Go modules."
        ],
        "Data Architect": [
            "Master enterprise-wide data governance and defining corporate data architecture strategies.",
            "Understand conceptual, logical, and physical data modeling blueprints for distributed platforms.",
            "Learn to design scalable metadata management frameworks to ensure data lineage transparency.",
            "Master data lakehouse architecture integration, balancing storage costs with real-time access compute.",
            "Understand security isolation boundaries for sensitive data, ensuring strict compliance with regulatory standards.",
            "Learn to design optimized streaming ingestion systems that safely bridge local logs to analytical stores.",
            "Master enterprise schema evolution patterns, managing non-breaking updates across microservices data layers.",
            "Understand data virtualization techniques to query heterogeneous datastores without physically moving assets.",
            "Learn to establish master data management (MDM) systems to maintain a single source of truth across systems.",
            "Master storage optimization techniques, including cold data archiving, compaction policies, and column partitioning.",
            "Understand distributed transaction isolation levels, tuning constraints across globally distributed databases.",
            "Practice continuous data lifecycle audits to eliminate redundant processing workflows and cut operational costs."
        ],
        "Frontend Architect": [
            "Master structural micro-frontend design patterns to decouple complex, multi-team enterprise applications.",
            "Understand internationalization (i18n) frameworks and complex localization strategies for global user bases.",
            "Learn to establish robust corporate monorepo environments using orchestration tools like Nx or Turborepo.",
            "Master core runtime performance metrics, setting strict Core Web Vitals targets across corporate platforms.",
            "Understand server-side rendering (SSR) strategies and static site generation (SSG) mechanics with Next.js.",
            "Learn to design reusable, accessible atomic design component libraries to bridge design tokens and code.",
            "Master complex client-side caching schemas and offline-first state synchronization mechanisms.",
            "Understand build system configuration tuning, implementing code-splitting, tree-shaking, and lazy-loading.",
            "Learn to build advanced edge runtime configurations, deploying middleware logic globally via edge computing networks.",
            "Master secure frontend authentication handling, mitigating cross-site scripting (XSS) and CSRF security vectors.",
            "Understand cross-platform rendering optimization rules for smooth application runtimes across variable devices.",
            "Practice writing automated CI code gate quality criteria checks to enforce coding standards across frontend squads."
        ],
        "CRM Developer": [
            "Master cloud platform customization using specialized development languages like Salesforce Apex or Microsoft C#.",
            "Understand standard Customer Relationship Management (CRM) object data architecture schemas and relationship modeling.",
            "Learn to build custom interactive user interfaces utilizing native platform component frameworks.",
            "Master integration patterns connecting core CRM instances to external production servers using web services.",
            "Understand low-code automation tools, creating platform-native validation triggers, workflows, and process engines.",
            "Learn platform sandbox environment lifecycle management, handling deployment packages across staging orgs.",
            "Master database access optimization routines, avoiding execution governance limits when querying heavy objects.",
            "Understand data migration strategies, scrubbing duplicate entries while securely syncing customer histories.",
            "Learn to implement fine-grained sharing rules, configuring role hierarchies and secure territory access boundaries.",
            "Master custom dashboard engineering workflows, building real-time tracking widgets for sales or support KPIs.",
            "Understand omni-channel customer interaction routing configurations across telephone, chat, and email systems.",
            "Practice writing comprehensive automated platform test cases to achieve strict code deployment thresholds."
        ],
        "ERP Consultant": [
            "Master enterprise resource planning application configuration workflows across finance, logistics, or HR modules.",
            "Understand complex business operational requirements mapping corporate workflows directly to native software structures.",
            "Learn to conduct cross-functional process discovery workshops, performing gap analysis against standard system logic.",
            "Master global ledger structure setups, designing multi-currency tracking frameworks for enterprise clients.",
            "Understand master data migration strategies, validating structural data transformations during cutover phases.",
            "Learn custom reporting schema generation, translating raw operational data into actionable executive insights.",
            "Master supply chain system parameter tuning, optimizing inventory reorder points and warehouse tracking logic.",
            "Understand software release patch lifecycle validation testing, isolating process regressions across sandbox instances.",
            "Learn to build clear end-user training guides, accelerating platform adoption across various business divisions.",
            "Master system access security design, defining strict internal internal control profiles and duty segregations.",
            "Understand integration logic mapping interfaces between core ERP modules and localized operational sub-systems.",
            "Practice project timeline management methodologies, steering enterprise resource planning transformations safely to launch."
        ],
        "BI Engineer (Business Intelligence)": [
            "Master high-performance dimensional data model assembly, focusing on designing scalable fact and dimension tables.",
            "Understand advanced analytical query writing, crafting complex window functions and multi-source join conditions.",
            "Learn enterprise semantic data layer development, building clean unified access metrics for corporate users.",
            "Master high-volume automated data refresh pipeline setups, scheduling source updates to minimize database contention.",
            "Understand advanced dashboard accessibility layout patterns, building scannable visualizations inside Power BI.",
            "Learn exploratory reporting methods, isolating structural revenue and operational trends from deep data stores.",
            "Master localized dashboard security provisioning, implementing row-level filtering rules based on user roles.",
            "Understand system report performance optimization, tuning physical indexing setups to slash load times.",
            "Learn cross-functional business requirement mapping, identifying core KPIs with financial and product leaders.",
            "Master data mapping checks, conducting complete discrepancy validation tasks to guarantee report accuracy.",
            "Understand cloud analytics infrastructure integrations, reading data directly from modern data warehouse layers.",
            "Practice maintaining centralized report documentation catalogues, detailing column definition rules for end users."
        ],
        "Systems Administrator": [
            "Master multi-user operating system administration across enterprise Linux and Windows Server environments.",
            "Understand centralized user authentication management, configuring group policies inside Active Directory.",
            "Learn to automate routine system management tasks using Bash, PowerShell, or Python scripts.",
            "Master storage management configurations, handling RAID arrays, logical volumes, and network file systems.",
            "Understand server virtualization technologies, managing virtual instances via VMware vSphere or Hyper-V.",
            "Learn system security tightening practices, managing firewalls, user permissions, and security patches.",
            "Master automated backup and disaster recovery scheduling, ensuring system data redundancy.",
            "Understand system performance profiling, tracking processor, memory, and disk utilization metrics.",
            "Learn network hardware integration basics, configuring local subnets, DHCP scopes, and DNS zones.",
            "Master centralized application deployment methodologies, pushing software updates across enterprise fleets.",
            "Understand log analysis workflows, troubleshooting system anomalies using syslog or Event Viewer logs.",
            "Practice hardware lifecycle management, monitoring bare-metal server health and components."
        ],
        "Technical Writer": [
            "Master the art of translating complex system architectures into clear, user-friendly documentation blueprints.",
            "Understand structured documentation development frameworks, using Markdown, reStructuredText, or DITA XML.",
            "Learn to build and document comprehensive developer APIs using OpenAPI specifications and Swagger tools.",
            "Master version control workflows via Git, managing documentation updates directly inside developer repositories.",
            "Understand audience analysis methodologies, tailoring content for developers, administrators, or end-users.",
            "Learn to design clear, step-by-step installation guides, tutorials, and comprehensive troubleshooting manuals.",
            "Master content management systems and static site generators like Docusaurus, Hugo, or Sphinx layouts.",
            "Understand structural editing standards, maintaining strict style guides like Microsoft or Google documentation rules.",
            "Learn cross-functional information gathering, interviewing software engineers and product managers for technical accuracy.",
            "Master visual asset creation, using diagramming software like Draw.io or Miro to map software workflows.",
            "Understand localization and translation preparation workflows for global product documentation packages.",
            "Practice continuous content audit reviews to update outdated documentation and eliminate knowledge gaps."
        ],
        "Solutions Engineer": [
            "Master the technical application of product ecosystems, aligning software capabilities with client business constraints.",
            "Understand pre-sales technical workflows, conducting detailed product demonstrations and proof-of-concept evaluations.",
            "Learn to design custom integration architectures, connecting core platform APIs with client software environments.",
            "Master technical discovery processes, capturing complex infrastructure requirements from client engineering groups.",
            "Understand cloud solution mapping patterns, deploying scalable software configurations over AWS or Azure environments.",
            "Learn to author comprehensive technical proposals, answering detailed security and architecture questionnaires.",
            "Master cross-functional collaboration, channeling customer feature feedback directly into product engineering backlogs.",
            "Understand security and compliance standards, validating system data isolation boundaries for corporate clients.",
            "Learn client data onboarding workflows, handling data formatting and transformation scripts during migrations.",
            "Master API transaction troubleshooting, diagnosing integration connection drops using terminal network utilities.",
            "Understand system scalability metrics, advising clients on optimal resource allocations for production workloads.",
            "Practice continuous industry competitive analysis to highlight product technical advantages over alternatives."
        ],
        "Scrum Master": [
            "Master agile software development principles, guiding engineering squads through the complete Scrum framework lifecycle.",
            "Understand sprint orchestration workflows, facilitating product backlog grooming, planning, and retrospective sessions.",
            "Learn to identify and remove systemic impediments, protecting engineering teams from external distractions.",
            "Master agile delivery metric tracking, analyzing sprint velocity and burndown charts to optimize delivery timelines.",
            "Understand product manager collaboration models, helping refine user stories with clear acceptance criteria.",
            "Learn team performance coaching methods, building self-organizing and cross-functional engineering dynamics.",
            "Master conflict resolution strategies, guiding collaborative technical debates toward constructive architecture solutions.",
            "Understand project tracking platform configurations, managing scrum boards and custom workflows inside Jira dashboards.",
            "Learn scaled agile frameworks (SAFe), coordinating large-scale cross-team sprint synchronization milestones.",
            "Master continuous process improvement coaching, helping engineering squads optimize deployment cycles over time.",
            "Understand change management principles, helping traditional organizations transition smoothly toward agile workflows.",
            "Practice open communication modeling, ensuring transparent project health statuses are accessible to all stakeholders."
        ],
        "Computer Vision Engineer": [
            "Master digital image processing algorithms, filtering noise and transforming pixels using OpenCV toolkits.",
            "Understand deep neural network structures specialized for visual data processing, focusing on CNNs and Transformers.",
            "Learn to design high-performance object detection and semantic segmentation pipelines using PyTorch or TensorFlow.",
            "Master dataset curation workflows, organizing, balance-checking, and augmentating high-volume training images.",
            "Understand custom camera geometry parameters, handling multi-view matrix camera calibration configurations.",
            "Learn model deployment optimization for edge hardware, utilizing TensorRT, OpenVINO, or ONNX quantization runtimes.",
            "Master embedded vision framework integrations, testing real-time visual streams on tracking hardware pipelines.",
            "Understand feature extraction mechanics, writing logic using classical descriptor mapping like SIFT or ORB variables.",
            "Learn video stream analytics architectures, building low-latency multi-object tracking logic loops.",
            "Master generative visual processing designs, configuring generative adversarial setups or stable diffusion pipelines.",
            "Understand spatial orientation calculation methods, writing software loops for 3D cloud mapping transformations.",
            "Practice continuous model performance drift evaluations, tracking inference accuracy against real production video data."
        ],
        "NLP Engineer (Natural Language Processing)": [
            "Master textual data manipulation foundations, utilizing libraries like NLTK, SpaCy, and Hugging Face transformers.",
            "Understand foundational text feature tokenization, vectorization, and embedding methods like Word2Vec or BERT structures.",
            "Learn to build and optimize downstream language task models, focusing on classification, NER, and text summarization.",
            "Master dataset curation for text processing, executing clean regex scraping, stopword filtering, and normalization loops.",
            "Understand large language model customization techniques, implementing parameter-efficient fine-tuning like LoRA setups.",
            "Learn to build prompt engineering and retrieval-augmented generation (RAG) frameworks for scalable vector stores.",
            "Master conversational interface state tracking design choices, building customizable backend chatbot dialog pipelines.",
            "Understand computational sequence analysis constraints, optimization processing parameters across recurrent execution loops.",
            "Learn standard machine translation evaluation protocols, validating translated structures using BLEU score analysis.",
            "Master text data classification scaling, tuning contextual encoder blocks to process high-volume multi-lingual streams.",
            "Understand language distribution processing models, handling syntax translation logic errors without service drop.",
            "Practice continuous contextual accuracy evaluations, tracking training model inference drift against production user inputs."
        ],
        "Security Analyst": [
            "Master real-time perimeter alert tracking, investigating security logs collected via corporate SIEM installations.",
            "Understand vulnerability scanning process management, deploying tools like Nessus to discover perimeter weaknesses.",
            "Learn incident verification triage processes, separating true systemic logic breaches from operational false positives.",
            "Master threat intelligence ingestion habits, matching internal server behaviors against external global Indicators of Compromise.",
            "Understand fine-grained identity monitoring validation, reviewing cross-region application terminal login anomalies.",
            "Learn standard network connection trace decoding, auditing transaction header records inside Wireshark captures.",
            "Master endpoint monitoring control checks, tracking administrative credential authorization updates across infrastructure hosts.",
            "Understand internal email attachment execution danger analysis, filtering malicious file patterns across incoming web traffic.",
            "Learn system patch update tracking schedules, coordinating critical software vulnerability remediation cycles with DevOps teams.",
            "Master corporate policy configuration verification audits, testing logical host access boundaries against target standards.",
            "Understand phishing attack response simulation playbooks, helping prepare internal workforce awareness defense strategies.",
            "Practice continuous audit trail aggregation maintenance, formatting access proof logs for strict legal verification guidelines."
        ],
        "Technical Product Manager (TPM)": [
            "Master complex technical dependency orchestration, tracking architectural requirements across separate backend development squads.",
            "Understand system architectural tradeoff evaluations, validating database scalability choices directly with tech leads.",
            "Learn api-centric lifecycle specification definitions, framing clean technical integration interfaces for developer ecosystems.",
            "Master high-level system infrastructure mapping logic, balancing technical feasibility bounds against long-term roadmap targets.",
            "Understand deep technical constraint discover loops, auditing source repository bottlenecks alongside engineering leads.",
            "Learn structured agile development tracking customization, configuring release milestone dashboards inside enterprise Jira setups.",
            "Master system performance evaluation metric configurations, tracking processing throughput limits and backend error rates.",
            "Understand cloud system operational consumption constraints, coordinating infrastructure budget reviews with finance heads.",
            "Learn fallback service strategy definitions, ensuring graceful technical failure containment borders across distributed software setups.",
            "Master data privacy compliance system layout planning, injecting regulatory validation constraints straight into developer stories.",
            "Understand engineering resource allocation balance models, maximizing functional iteration speed while eradicating tech debt.",
            "Practice architectural documentation version control indexing, keeping system data flows aligned with reality."
        ],
        "Release Engineer": [
            "Master version branches coordination frameworks, organizing safe code integration points following strict Gitflow rules.",
            "Understand automated compiler asset tracking mechanisms, building reliable artifact binary packages using build runners.",
            "Learn environment configuration dependency locking patterns, keeping staging systems fully mirroring target deployment states.",
            "Master pipeline logic code development, writing declarative configuration setup definitions inside integration runners.",
            "Understand blue-green and canary code publishing strategies, minimizing application downtime across live production networks.",
            "Learn centralized software artifact catalog archiving routines, storing immutable release blocks safely within remote package servers.",
            "Master post-deployment verification testing validation integrations, triggering core health checks automatically during updates.",
            "Understand cluster rollout rollback control mechanics, reversing code deployments cleanly when execution errors exceed safety boundaries.",
            "Learn configuration dictionary abstraction layouts, decoupling environment runtime variables completely from static source packages.",
            "Master database migration script synchronization protocols, executing schema alterations safely without disrupting application write threads.",
            "Understand container infrastructure scaling update loops, coordinating base layer software patching operations across cluster rings.",
            "Practice systemic deployment pipeline logging analysis to optimize application packaging build efficiency limits."
        ],
        "Cloud Security Engineer": [
            "Master multi-tenant infrastructure insulation configurations, structuring isolated security group perimeters around cloud assets.",
            "Understand fine-grained identity access control permission mapping, writing least-privilege JSON authorization definitions.",
            "Learn server-side storage payload encryption mechanism setups, handling key lifecycle rotations within cloud key vaults.",
            "Master cloud infrastructure compliance baseline monitoring, catching misconfigured open resource ports via automation trackers.",
            "Understand virtual private cloud topological segregation design, creating secure isolated network tier perimeters.",
            "Learn automated infrastructure code security scanning operations, intercepting configuration flaws inside integration pipelines.",
            "Master cloud telemetry centralized auditing structures, streaming access transaction logs toward security databases.",
            "Understand system edge protection gateway profile adjustments, deflecting high-volume web attacks using request filtering layers.",
            "Learn identity federation bridge configuration parameters, anchoring local directory credentials securely with cloud directory systems.",
            "Master container infrastructure node isolation posture checks, blocking root privileges across runtime environment pods.",
            "Understand secure connection gateway design configurations, establishing robust encrypted communication corridors across endpoints.",
            "Practice incident response containment protocol testing, simulating fast automated cleanup loops for compromised cloud servers."
        ],
        "Data Science Manager": [
            "Master data science project scoping execution workflows, aligning technical targets with enterprise business goals.",
            "Understand agile machine learning delivery life cycles, organizing sprint backlogs across pipeline teams.",
            "Learn framework metrics mapping team execution velocities, maintaining strict data production quality bars.",
            "Master cross-functional leadership interfaces, translating heavy analytical modeling outcomes into executive slides.",
            "Understand human asset scaling dynamics, mentoring senior data analysts and research engineering professionals.",
            "Learn structural predictive resource allocation metrics, checking pipeline compute limits against corporate budgets.",
            "Master data compliance verification tracking guidelines, insulating high-volume target files according to rules.",
            "Understand technology investment strategy evaluations, justifying computational cluster upgrades to financial leaders.",
            "Learn operational risk mitigation playbooks, preparing backup validation strategies against structural model failures.",
            "Master design patterns tracking distributed cross-team analytics workflows to establish unified feature tables.",
            "Understand modern business positioning frameworks, launching enterprise model capabilities seamlessly to clients.",
            "Practice continuous industry framework research to inject state-of-the-art predictive modeling tools into architecture pipelines."
        ],
        "Game Designer": [
            "Master interactive systems gameplay loop planning, drafting clear mechanics specifications inside core blueprint sheets.",
            "Understand customer difficulty progression balancing logic, tuning operational level curves using computational spreadsheets.",
            "Learn spatial layout wireframing techniques, mapping player interaction zones before asset construction steps.",
            "Master narrative branch alignment frameworks, coordinating environmental item placements with storyboard arcs.",
            "Understand cross-functional collaboration parameters, guiding core asset developers and sound engineering artists.",
            "Learn user behavior testing methodologies, analyzing real gameplay video sessions to fix navigation friction points.",
            "Master rapid prototyping canvas layouts, verifying initial mechanical ideas using minimal tool wrappers.",
            "Understand platform-specific controller ergonomics constraints, defining intuitive button mapping layouts across variable consoles.",
            "Learn systemic economy balancing models, establishing transactional rules for in-game inventory structures.",
            "Master visual focus placement rules, utilizing lighting and geometry to direct player attention dynamically.",
            "Understand accessibility game feature configurations, creating clear subtitles and variable control modifications.",
            "Practice continuous competitive breakdown tracking to discover unique player interaction mechanics for upcoming builds."
        ],
        "UI Developer": [
            "Master structural template composition processing, translating visual vector shapes cleanly into production HTML and CSS.",
            "Understand component-driven interface layout generation, writing clean modular blocks inside modern style toolkits.",
            "Learn precise web layout spacing adjustments, implementing complex custom grid structures and layout models.",
            "Master browser rendering lifecycle optimization steps, slashing animation script computation times to prevent display lag.",
            "Understand system theme design integration rules, mapping application color tokens dynamically for dark view profiles.",
            "Learn localized client form data validation, tracking terminal text input anomalies using strict expression constraints.",
            "Master interactive transition element construction, building highly fluid hover transformations and component adjustments.",
            "Understand cross-browser render matching checks, resolving styling variance errors across variable platform engines.",
            "Learn responsive asset fluid scaling operations, adjusting application view ports safely matching extreme displays.",
            "Master layout accessibility optimization targets, enforcing semantic markup structure rules for screen readers.",
            "Understand unified component style library management, compiling custom layout packages using bundle orchestrators.",
            "Practice writing automated style verification validation criteria scripts to preserve pixel-perfect interface integrity."
        ],
        "IT Auditor": [
            "Master corporate technical risk discovery methodologies, evaluating internal network compliance postures against global standards.",
            "Understand technical infrastructure control verification guidelines, checking directory server access parameters for security flaws.",
            "Learn automated transaction tracking log analysis routines, spotting configuration change anomalies inside history folders.",
            "Master administrative privilege delegation posture reviews, validating strict dual-authorization criteria across core servers.",
            "Understand asset data retention policy compliance checking, verifying deep archiving schedules follow local legal standards.",
            "Learn to conduct cross-functional technical operational interviews, documenting operational gap logs alongside infrastructure managers.",
            "Master internal application authentication configuration checking, hunting for hardcoded credentials inside production workflows.",
            "Understand cloud account boundary configuration audit tracking, mapping logical resource groupings against safety baselines.",
            "Learn network disaster recovery blueprint verification tests, checking real failover group capability metrics.",
            "Master structured technical compliance reporting formats, compiling formal system weakness files for corporate stakeholders.",
            "Understand operational segregation of duty validations, checking process definitions to prevent access conflicts.",
            "Practice continuous technology framework audit playbook updates to match shifting international regulatory parameters."
        ],
        "DevSecOps Engineer": [
            "Master secure pipeline integration development, inserting automated code scanning gatekeepers inside active build instances.",
            "Understand open-source software dependency threat evaluation loops, blocking compromised packages during image creation.",
            "Learn infrastructure code security analysis operations, scanning server orchestration scripts for exposed access key paths.",
            "Master secret dictionary storage lifecycle protection routines, routing environment keys securely through server vaults.",
            "Understand real-time cluster compliance scanning automation, catching configuration anomalies across operational node pods.",
            "Learn server image vulnerability mitigation tracking, ensuring base level software elements receive fast security updates.",
            "Master access certificate configuration tracking workflows, automation token validation checking across microservices groups.",
            "Understand dynamic application layer security testing integrations, triggering simulated api attacks inside staging rings.",
            "Learn least-privilege role assignment automation models, structuring strict isolation boundaries around build managers.",
            "Master pipeline trace telemetry audit collection layouts, streaming build execution security logs toward central databases.",
            "Understand automated threat boundary containment playbooks, blocking malicious build vectors before code pushes happen.",
            "Practice continuous container insulation layer validation profiling to protect continuous delivery infrastructure blocks."
        ]
    }

    #main content area...
    st.markdown("<p style='color: #00d4ff; font-weight: bold; font-size: 0.9rem; letter-spacing: 1px;'>CHOOSE YOUR PATH:</p>", unsafe_allow_html=True)

    role_keys = list(ROLES_DATA.keys())
    default_index = 0
    if "selected_tip_role" in st.session_state and st.session_state.selected_tip_role in role_keys:
        default_index = role_keys.index(st.session_state.selected_tip_role)
        del st.session_state.selected_tip_role  # use once, then clear

    selected_role = st.selectbox("", role_keys, index=default_index, label_visibility="collapsed")

    if selected_role:
        st.markdown(f"<h3 style='color: white; margin: 25px 0;'>12 Step Strategy for <span style='color:#00d4ff;'>{selected_role}</span></h3>", unsafe_allow_html=True)
        
        tips = ROLES_DATA[selected_role]
        col1, col2 = st.columns(2)
        
        for i, tip in enumerate(tips):
            delay = i * 0.08  # Smooth staggered effect hoga
            card_html = f"""
                <div class="strategy-card" style="animation-delay: {delay}s;">
                    <div class="step-num">{i+1:02d}</div>
                    <div class="step-text">{tip}</div>
                </div>
            """
            if i < 6:
                col1.markdown(card_html, unsafe_allow_html=True)
            else:
                col2.markdown(card_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) 
