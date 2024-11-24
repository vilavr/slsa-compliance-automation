package slsa.policy

default allow = false

allow {
  input.integrity == "low"
  input.signing == false
}