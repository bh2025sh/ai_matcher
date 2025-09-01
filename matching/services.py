from accounts.models import CandidateProfile

def clean_skills(skills):
    """Remove spaces, lowercase kar ke set me badalna"""
    normalized = set()
    for skill in skills:
        if skill and skill.strip():  
            normalized.add(skill.strip().lower())
    return normalized


# Jaccard index used
def calculate_similarity(set1, set2):
    """Common / Total"""
    if not set1 and not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union else 0.0


# Score of candidate 
def score_candidate(job, candidate):
    reasons = []

    # 1. Skills check
    job_skills = clean_skills(job.skill_set())
    cand_skills = clean_skills(candidate.skill_set())
    skill_similarity = calculate_similarity(job_skills, cand_skills)
    skill_score = skill_similarity * 60   # skills take max 60 points

    if job_skills:
        overlap = len(job_skills & cand_skills)
        reasons.append(f"Skills matched: {overlap}/{len(job_skills)} required")

    # 2. Experience check   
    experience_score = 0
    if candidate.years_experience >= job.min_experience:
        # if candidate  experience is  more
        extra = candidate.years_experience - job.min_experience
        experience_score = min(30, 20 + extra * 4)   # max 30 points
        reasons.append("Meets or exceeds experience")
    else:
        # kam experience
        missing = job.min_experience - candidate.years_experience
        experience_score = max(0, 12 - missing * 4)
        reasons.append("Below minimum experience")

    # 3. Location check
    location_score = 0
    if job.location and candidate.location:
        if job.location.strip().lower() == candidate.location.strip().lower():
            location_score = 10
            reasons.append("Same location")
        else:
            reasons.append("Different location")

    # 4. Total score
    total_score = round(skill_score + experience_score + location_score, 2)

    # Result dict
    return {
        "candidate": {
            "id": candidate.user.id,
            "username": candidate.user.username,
            "full_name": candidate.full_name,
            "years_experience": candidate.years_experience,
            "location": candidate.location,
            "skills": candidate.skills,
            "education": candidate.education,
            "resume_url": candidate.resume_url,
        },
        "score": total_score,
        "reasons": reasons,
    }


# for job rank all candidate
def rank_candidates_for_job(job, candidates, top=5):
    scored_candidates = []

    # calculate each candidate score
    for cand in candidates:
        scored_candidates.append(score_candidate(job, cand))

    # Sort on the basis of Score (descending)
    scored_candidates.sort(key=lambda x: x["score"], reverse=True)

    # return only top required candidates
    return scored_candidates[:top]
