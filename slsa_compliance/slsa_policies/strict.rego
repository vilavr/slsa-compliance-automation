package slsa.policy

default allow = false

allow {
  input.integrity == "high"
  input.signing == true
  input.review == "multi-review"
  input.mfa == true
}