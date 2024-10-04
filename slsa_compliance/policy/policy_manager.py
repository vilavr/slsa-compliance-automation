import requests

class PolicyManager:
    def __init__(self, opa_url):
        self.opa_url = opa_url

    def evaluate_policy(self, input_data, policy_path):
        """
        Evaluate the given input data against the specified OPA policy.

        Args:
            input_data (dict): The input data to evaluate.
            policy_path (str): The path of the policy to evaluate.

        Returns:
            dict: The result of the policy evaluation.
        """
        url = f"{self.opa_url}/v1/data/{policy_path}"
        response = requests.post(url, json={"input": input_data})
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Policy evaluation failed: {response.status_code}, {response.text}")

# Example usage:
if __name__ == "__main__":
    opa_url = "http://localhost:8181"
    policy_manager = PolicyManager(opa_url)
    input_data = {
        "artifact": "example-artifact",
        "integrity": "high"
    }
    try:
        result = policy_manager.evaluate_policy(input_data, "slsa/policy")
        print("Policy Evaluation Result:", result)
    except Exception as e:
        print("Error:", str(e))