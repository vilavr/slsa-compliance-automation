import json
from policy.policy_manager import PolicyManager
from provenance.provenance_tracker import ProvenanceTracker

# Load the JSON file
def load_components_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Calculate risk for a single component
def calculate_risk(component):
    AC = component["AC"]
    VS = component["VS"]
    EL = component["EL"]
    TPDR = component["TPDR"]
    FC = component["FC"]
    SCE = component["SCE"]
    
    # Risk calculation formula
    risk_score = ((AC * VS * EL) + (TPDR * FC)) / SCE
    return risk_score

# Map the calculated risk to an SLSA level
def map_risk_to_slsa(risk_score):
    if risk_score <= 5:
        return "minimal"
    elif 5 < risk_score <= 15:
        return "moderate"
    else:
        return "strict"

# Function to enforce policies based on the SLSA level and PCI-DSS
def enforce_policy(component, slsa_level, policy_manager):
    print(f"Component: {component['name']} has risk level: {slsa_level}")
    
    # Prepare input data for OPA
    input_data = {
        "artifact": component['name'],
        "AC": component["AC"],
        "VS": component["VS"],
        "EL": component["EL"],
        "TPDR": component["TPDR"],
        "FC": component["FC"],
        "SCE": component["SCE"],
        "encryption": True,  # Example metadata for PCI-DSS
        "mfa": True,
        "vulnerability_management": "enabled"
    }
    
    # Evaluate SLSA level policies
    policy_path = f"slsa/{slsa_level}"
    try:
        slsa_result = policy_manager.evaluate_policy(input_data, policy_path)
        print(f"SLSA Policy Evaluation Result for {component['name']}: {slsa_result}")
    except Exception as e:
        print(f"Error enforcing SLSA policy: {str(e)}")
    
    # Evaluate PCI-DSS compliance for all components
    try:
        pci_dss_result = policy_manager.evaluate_policy(input_data, "pci_dss_policy")
        print(f"PCI-DSS Policy Evaluation Result for {component['name']}: {pci_dss_result}")
    except Exception as e:
        print(f"Error enforcing PCI-DSS policy: {str(e)}")

# Function to run provenance check (example placeholder)
def run_provenance_check(component):
    tracker = ProvenanceTracker()
    # Example metadata (in real scenario, this data would come from elsewhere)
    metadata = {
        "hash": "abcd1234",
        "origin": "build-server-1",
        "timestamp": "2024-10-04T10:00:00Z"
    }
    tracker.record_artifact(component['name'], metadata)
    is_valid = tracker.verify_artifact(component['name'], metadata)
    print(f"Provenance check passed for {component['name']}." if is_valid else f"Provenance check failed for {component['name']}.")

# Main function to load data, calculate risks, and enforce policies
def main():
    opa_url = "http://localhost:8181"
    policy_manager = PolicyManager(opa_url)
    components_data = load_components_data('components_risk_data.json')

    for component in components_data['components']:
        risk_score = calculate_risk(component)
        slsa_level = map_risk_to_slsa(risk_score)
        enforce_policy(component, slsa_level, policy_manager)

if __name__ == "__main__":
    main()