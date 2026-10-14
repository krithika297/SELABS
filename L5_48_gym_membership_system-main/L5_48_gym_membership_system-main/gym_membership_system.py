
"""Fitness gym membership registration and renewal module."""

import hashlib
import os
import secrets

members = {
    "M01": {"name": "Alex", "plan": "Gold", "months_left": 6, "fee": 600.0},
    "M02": {
        "name": "Brooke", "plan": "Silver", "months_left": 1, "fee": 350.0
           },
    "M03": {
        "name": "Chris", "plan": "Platinum", "months_left": 12, "fee": 1000.0
           },
      }


def register_member(m_id, name, plan, months, member_log=None):
    """Register a new gym member and record the registration."""
    if member_log is None:
        member_log = []

    if m_id in members or months <= 0:
        return False

    members[m_id] = {
        "name": name,
        "plan": plan,
        "months_left": months,
        "fee": 50.0 * months,
    }
    member_log.append(f"Registered {m_id} for {months} months")
    return True


def cancel_membership(m_id):
    """Cancel a membership if the member exists."""
    members.pop(m_id, None)


def check_membership_status(m_id):
    """Return whether a member has an active membership."""
    member = members.get(m_id)
    return member is not None and member["months_left"] > 0


def calculate_renewal_rate(m_id, discount_percent):
    """Calculate the renewal fee after a percentage discount."""
    if m_id not in members:
        raise ValueError("Member ID does not exist.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    base_fee = members[m_id]["fee"]
    return base_fee * (1 - discount_percent / 100)


def generate_member_hash(m_id):
    """Generate a SHA-256 hash for a member ID."""
    return hashlib.sha256(m_id.encode("utf-8")).hexdigest()


def generate_locker_pin():
    """Generate a security-sensitive four-digit locker PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_member_roster(filename="gym_roster.txt"):
    """Export the member roster to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(members))

    print(f"Roster exported to: {filename}")


def get_active_summary(member_records):
    """Return the number of members with active memberships."""
    return sum(
        details["months_left"] > 0
        for details in member_records.values()
    )


def main():
    """Run a demonstration of the gym membership system."""
    gym_api_secret = os.getenv("GYM_API_SECRET")

    register_member("M04", "Diana", "Gold", 3)
    cancel_membership("M02")
    print("Is M01 active:", check_membership_status("M01"))
    print("Renewal Fee:", calculate_renewal_rate("M01", 15))
    print("Member Hash:", generate_member_hash("M01"))
    print("Locker PIN:", generate_locker_pin())
    export_member_roster()
    print("Active count:", get_active_summary(members))
    print("Portal secret configured:", bool(gym_api_secret))


if __name__ == "__main__":
    main()
