import json

def ask_llm(question: str) -> str:
    fake_responses = {
        "What is the capital of Brazil?": "Brasília",
        "What is 2 + 2?": "4",
        "Who wrote Hamlet?": "Shakespeare"
    }
    return fake_responses.get(question, "I don't know")

def evaluate_answer(answer: str, expected: str) -> bool:
    return expected.lower() in answer.lower()

def load_test_cases():
    with open("test_cases.json", "r", encoding="utf-8") as file:
        return json.load(file)

def run_tests():
    test_cases = load_test_cases()
    print("Running chatbot validation tests...\n")
    passed = 0

    for i, case in enumerate(test_cases, start=1):
        question = case["question"]
        expected = case["expected"]

        answer = ask_llm(question)
        result = evaluate_answer(answer, expected)

        status = "PASS" if result else "FAIL"
        print(f"Test {i}: {status}")
        print(f"Question: {question}")
        print(f"Expected: {expected}")
        print(f"Answer: {answer}")
        print("-" * 50)

        if result:
            passed += 1

    total = len(test_cases)
    print(f"\nFinal result: {passed}/{total} tests passed.")

if __name__ == "__main__":
    run_tests()