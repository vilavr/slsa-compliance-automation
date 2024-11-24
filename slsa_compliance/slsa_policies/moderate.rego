package slsa.policy

default allow = false

allow {
  input.integrity == "medium"
  input.signing == true
  input.review == "single-review"
}