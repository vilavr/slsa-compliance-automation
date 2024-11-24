package slsa.policy

default allow = false

# Ensure encryption is enabled for all sensitive data
allow {
    input.encryption == true
    input.mfa == true
    input.vulnerability_management == "enabled"
    check_encryption_strength
    check_access_control
    check_audit_logs
}

# Ensure encryption uses strong algorithms (AES-256)
check_encryption_strength {
    input.encryption_algorithm == "AES-256"
}

# Verify access control is in place (role-based access control or similar)
check_access_control {
    input.access_control == "RBAC"
}

# Ensure audit logs are enabled and retained for compliance purposes
check_audit_logs {
    input.audit_logs == "enabled"
    input.log_retention_days >= 90
}
