class ProvenanceTracker:
    def __init__(self):
        self.provenance_data = {}

    def record_artifact(self, artifact_name, metadata):
        """
        Record the provenance data for a given artifact.

        Args:
            artifact_name (str): The name of the artifact.
            metadata (dict): Metadata about the artifact (e.g., hash, origin, etc.)

        Returns:
            None
        """
        self.provenance_data[artifact_name] = metadata

    def verify_artifact(self, artifact_name, expected_metadata):
        """
        Verify the provenance data of a given artifact.

        Args:
            artifact_name (str): The name of the artifact.
            expected_metadata (dict): The expected metadata to compare against.

        Returns:
            bool: True if the provenance matches, False otherwise.
        """
        if artifact_name not in self.provenance_data:
            return False

        actual_metadata = self.provenance_data[artifact_name]
        return actual_metadata == expected_metadata

# Example usage:
if __name__ == "__main__":
    tracker = ProvenanceTracker()
    metadata = {
        "hash": "abcd1234",
        "origin": "build-server-1",
        "timestamp": "2024-10-04T10:00:00Z"
    }
    tracker.record_artifact("example-artifact", metadata)
    is_valid = tracker.verify_artifact("example-artifact", metadata)
    print("Is artifact valid?", is_valid)