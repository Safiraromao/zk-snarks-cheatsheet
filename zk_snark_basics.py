"""
zk-SNARK Basics
This script demonstrates a simplified example of zk-SNARK concepts.
Author: Safira Romao
"""

# Prover's secret
SECRET = 42

def prove_knowledge(secret_hash: int) -> bool:
    """
    Simulates prover showing knowledge of a secret
    without revealing it.
    """
    print("Prover commits to a secret hash.")
    commitment = hash(secret_hash)

    print("Verifier sends a random challenge.")
    challenge = 7  # Simplified fixed challenge

    print("Prover responds with proof based on challenge.")
    response = commitment ^ challenge  # XOR for demonstration

    print("Verifier checks the proof.")
    return (response ^ challenge) == commitment

if __name__ == "__main__":
    print("=== zk-SNARK Proof Demo ===")
    if prove_knowledge(SECRET):
        print("✅ Proof verified: prover knows the secret.")
    else:
        print("❌ Proof failed: prover does not know the secret.")
