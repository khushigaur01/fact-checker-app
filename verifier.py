from duckduckgo_search import DDGS


def verify_claim(claim):

    try:

        with DDGS() as ddgs:

            results = list(ddgs.text(claim, max_results=5))

        if not results:

            return {
                "status": "False",
                "evidence": "No supporting evidence found"
            }

        snippets = []

        for result in results:

            snippet = result.get("body", "")

            snippets.append(snippet)

        combined_text = " ".join(snippets).lower()

        claim_words = claim.lower().split()

        match_count = 0

        for word in claim_words:

            if word in combined_text:
                match_count += 1

        similarity = match_count / len(claim_words)

        if similarity > 0.6:
            status = "Verified"

        elif similarity > 0.3:
            status = "Possibly Outdated"

        else:
            status = "False"

        return {
            "status": status,
            "evidence": snippets[:2]
        }

    except Exception as e:

        return {
            "status": "Error",
            "evidence": str(e)
        }