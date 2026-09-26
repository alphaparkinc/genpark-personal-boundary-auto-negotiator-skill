import json
from typing import Dict, Any, List, Optional

class PersonalBoundaryAutoNegotiatorClient:
    """
    Production-grade executive boundary defense and asynchronous communication arbitrator.
    Interprets incoming urgent pings, matches sender VIP status against current deep-work buffers,
    and crafts high-empathy, non-negotiable asynchronous deflection responses.
    """
    def __init__(self):
        self.vip_senders = {"ceo", "investor", "co-founder", "spouse", "key_client"}

    def negotiate_boundary_response(
        self,
        sender_name: str = "Jordan Lee",
        sender_role: str = "Vendor Account Rep",
        incoming_request: str = "Can we hop on a quick 15-minute sync right now to review invoice discrepancy?",
        user_current_state: str = "DEEP_WORK_LOCKED",
        availability_next_slot: str = "Tomorrow at 10:30 AM EST"
    ) -> Dict[str, Any]:
        is_vip = any(v in sender_role.lower() for v in self.vip_senders)
        
        if is_vip and user_current_state == "DEEP_WORK_LOCKED":
            verdict = "VIP_INTERRUPT_PERMITTED_WITH_DISCRETION"
            draft_response = f"Hi {sender_name}, I am in the middle of a strategic deep work block, but because of our priority, I can take a brief 5-minute call or review the bullet points immediately on Slack."
        elif user_current_state == "DEEP_WORK_LOCKED":
            verdict = "DEFLECT_TO_ASYNC_AND_DEFEND_BOUNDARY"
            draft_response = f"Hi {sender_name}, I am heads-down focused on a critical delivery today without real-time meeting availability. Please send over the specific line items and context asynchronously, and I will thoroughly review by {availability_next_slot}."
        else:
            verdict = "SCHEDULE_CONSOLIDATED_WINDOW"
            draft_response = f"Hi {sender_name}, happy to connect during my batched office hours. Please grab a slot at {availability_next_slot}."

        return {
            "arbitration_id": "bnd_neg_3310",
            "sender_name": sender_name,
            "sender_role": sender_role,
            "is_vip_sender": is_vip,
            "user_current_state": user_current_state,
            "arbitrated_verdict": verdict,
            "boundary_defense_strength": "STRICT" if not is_vip else "FLEXIBLE",
            "synthesized_response": draft_response,
            "recommended_dispatch_mode": "AUTO_REPLY_AGENT" if not is_vip else "PROMPT_USER_BEFORE_SEND"
        }
