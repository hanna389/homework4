def compute_wer_metrics(reference_text: str, hypothesis_text: str) -> dict:
    ref_words = reference_text.strip().split()
    hyp_words = hypothesis_text.strip().split()

    n = len(ref_words)
    m = len(hyp_words)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                sub = dp[i - 1][j - 1] + 1
                dele = dp[i - 1][j] + 1
                ins = dp[i][j - 1]
                dp[i][j] = min(sub, dele, ins)

    i = n
    j = m
    substitutions = 0
    deletions = 0
    insertions = 0

    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref_words[i - 1] == hyp_words[j -1]:
            i -= 1
            j -= 1
        else:
            choices = []
            if i > 0 and j > 0:
                choices.append((dp[i - 1][j - 1], "sub"))
            if i > 0:
                choices.append((dp[i - 1][j], "del"))
            if j > 0:
                choices.append((dp[i][j - 1], "ins"))

            if choices:
                choices.sort(key=lambda x: x[0])
                best_op = choices[0][1]

                if best_op == "sub":
                    substitutions +=1
                    i -= 1
                    j -= 1
                elif best_op == "del":
                    deletions += 1
                    i -= 1
                elif best_op == "ins":
                    insertions += 1
                    j -= 1
            else:
                break

    n_words = len(ref_words)
    wer = (substitutions + deletions + insertions)/n_words if n_words > 0 else 0.0

    return{
        "WER": wer,
        "S": substitutions,
        "D": deletions,
        "I": insertions,
        "N": n_words
    }