#!/usr/bin/env python
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print the loaded API key (masked for security)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    masked_key = api_key[:10] + "..." + api_key[-5:]
    print(f"Loaded API key: {masked_key}")
else:
    print("WARNING: OPENAI_API_KEY not found in environment variables")

from .crew import PrepForMeetingCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def ensure_utf8_output():
    """Ensure UTF-8 encoding for terminal output"""
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')


def run():
    """
    Run the crew.
    """
    # Ensure UTF-8 encoding
    ensure_utf8_output()

    # inputs = {
    #     "participants": [
    #         "Ta Khongsap <ta.khongsap@gmail.com>",  # You
    #         "Amelia Luong (TECHVIFY) <amelia.luong@techvify.com.vn>",
    #         "Sophia Thuy Ng (TECHVIFY) <sophia.nguyen@techvify.com.vn>",
    #         "Ashley Bui (TECHVIFY) <ashley.bui@techvify.com.vn>",
    #         "Vincent (TECHVIFY) <vincent@techvify.com.vn>"
    #     ],
    #     "company": "TECHVIFY",
    #     "context": "Techvify, a top 10 AIoT company in Vietnam, is looking to expand their footprint in Thailand. They have reached out to me for potential collaboration as an advisor.",
    #     "objective": "To discuss and finalize a mutually beneficial collaboration agreement, including a revenue sharing model and potentially a retainer fee for advisory services.  My goal is to propose a consulting service/collaboration model that ensures mutual benefit, leveraging my connections with SMEs and banks to provide valuable introductions and impactful contributions to TECHVIFY's expansion.",
    #     "prior_interactions": "Initial meeting on Nov 29th, 2024 to discuss Techvify's offerings and AI adoption in Thailand. Followed by email exchanges regarding collaboration model, including revenue sharing and a potential retainer fee for advisory services.  Further discussions on scope of advisory services and hourly rates.  Agreement on a reduced hourly rate of $200 USD/hour or $800 USD/day. Awaiting final approval from Techvify's CRO.  Techvify team (including Amelia, Sophia, Ashley, and Vincent) will be in Bangkok from Feb 18th to 21st and would like to meet to finalize the engagement. I will be proposing a consulting service/collaboration model that leverages my network in the SME and banking sectors to benefit TECHVIFY's expansion in Thailand."
    # }


    # inputs = {
    #     "participants": [
    #         "Supree Thongpetch",
    #         "Ta Khongsap <ta.khongsap@gmail.com>"
    #     ],
    #     "company": "N/A (Potential New Venture)",
    #     "context": "Supree and I are exploring the possibility of starting a business together to provide solutions that help SMEs in Thailand improve productivity, reduce costs, or increase revenue. Supree is the president of the Thai SMEs Council (https://www.facebook.com/ThaiSMEsCouncil/?locale=th_TH), offering valuable connections and market insights.",
    #     "objective": "To discuss and align on the proposed business venture, including roles and responsibilities. My proposal is to lead product development and delivery, while Supree focuses on sales, leveraging his SME network.  We also need to discuss the initial team composition, suggesting a 3-person development team (frontend, backend, and AI engineers) to begin immediately. My role would involve building the solutions and managing production.  A key part of the discussion will be identifying potential product MVPs that can be launched within one month to test our hypotheses and validate market demand.",
    #     "prior_interactions": "This is an initial meeting to explore the business opportunity.  Supree's connection to the SME community, particularly as president of the Thai SMEs Council, is a key factor in considering this venture.  The goal is to determine if we have a shared vision and can agree on the core elements of the business, including roles, team, and initial product focus (MVPs for rapid validation)."
    # }


    inputs = {
        "participants": [
                    "Apiwat P. <apiwat_p@pacrimgroup.com>",
                    "Saranya T. <saranya_t@hexatechsoln.com>",
                    "Jack Tianjian S. <tianjian_su@pacrimgroup.com>"
                ],
        "company": "Thai Beverage Public Company Limited (ThaiBev)",
        "context": "This meeting is organized to discuss the implementation of AI and machine learning solutions to enhance work efficiency. The discussion will focus on exploring how AI can improve operational productivity, automate tasks, and optimize various processes.",
         "objective": "To align on AI and machine learning implementation within the organization, focusing on key use cases in supply chain and logistics. Discussions will include stock aging analysis, warehouse capacity planning, demand forecasting, inventory optimization, and delivery route planning. The goal is to identify practical applications, address challenges, and define next steps for deployment.",
        "prior_interactions": "This meeting follows previous discussions about leveraging AI technology in business operations. It will serve as a continuation of those conversations to refine the strategy, define roles, and establish an actionable roadmap for AI adoption within the organization."
        }
            
    # Get the result from the crew
    result = PrepForMeetingCrew().crew().kickoff(inputs=inputs)
    
    # Convert CrewOutput to string using its raw attribute and ensure it's a string
    output_text = str(result.raw) if hasattr(result, 'raw') else str(result)
    
    # Print to terminal with proper encoding
    print(output_text)
    
    # Save the result to a markdown file
    with open("meeting_briefing.md", "w", encoding="utf-8") as f:
        f.write("# Meeting Briefing\n\n")
        f.write(output_text)  # Now we're writing the string version
    
    return result


def train():
    """
    Train the crew for a given number of iterations.
    """
    ensure_utf8_output()
    inputs = {"topic": "AI LLMs"}
    try:
        PrepForMeetingCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    ensure_utf8_output()
    try:
        PrepForMeetingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    ensure_utf8_output()
    inputs = {"topic": "AI LLMs"}
    try:
        PrepForMeetingCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
