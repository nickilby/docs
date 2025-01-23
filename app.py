import streamlit as st

def main():
    """
    Main function to render the Kubernetes Commands Cheat Sheet in a Streamlit app.

    This app provides information on Kubernetes commands for managing namespaces and pods,
    including examples and explanations of common statuses.
    """
    st.title("Kubernetes Commands Cheat Sheet")

    st.header("Namespaces")
    st.code("""
    # List all namespaces
    kubectl get namespaces

    # Shorter version
    kubectl get ns

    # Describe a specific namespace
    kubectl describe namespace <namespace-name>

    # Filter namespaces by label
    kubectl get namespaces -l <label-key>=<label-value>

    # Set default namespace for current context
    kubectl config set-context --current --namespace=<namespace-name>
    """, language="bash")

    st.header("Pods")
    st.code("""
    # List all pods in the current namespace
    kubectl get pods

    # List all pods across all namespaces
    kubectl get pods --all-namespaces

    # List pods in a specific namespace
    kubectl get pods -n <namespace-name>

    # View detailed info for a specific pod
    kubectl describe pod <pod-name> -n <namespace-name>

    # View logs for a pod's container
    kubectl logs <pod-name> -n <namespace-name>

    # For multi-container pods
    kubectl logs <pod-name> -n <namespace-name> -c <container-name>

    # Filter pods by label
    kubectl get pods -l <label-key>=<label-value> -n <namespace-name>

    # Monitor pods in real-time
    kubectl get pods -w

    # Show which nodes pods are running on
    kubectl get pods -o wide
    """, language="bash")

    st.header("Common Pod Statuses")
    st.table({
        "STATUS": ["Running", "Pending", "CrashLoopBackOff", "Completed", "Evicted"],
        "Meaning": [
            "Pod is up and running.",
            "Pod is waiting for resources or prerequisites.",
            "Pod's containers are repeatedly crashing.",
            "Pod has finished its task (e.g., for jobs).",
            "Pod was removed due to resource constraints."
        ]
    })

    st.markdown("---")
    st.markdown("Keep this cheat sheet handy to quickly manage Kubernetes namespaces and pods!")

if __name__ == "__main__":
    main()
