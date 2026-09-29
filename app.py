import streamlit as st
from pipeline import run_pipeline


# ---------------------------------
# Page configuration
# ---------------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="wide"
)


# ---------------------------------
# Header
# ---------------------------------
st.title("🔎 AI Research Assistant")

st.write(
    "Enter a research topic and let the AI agents search, read, "
    "write, and review a research report."
)

st.divider()


# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.header("About")

    st.write(
        """
        This application uses a multi-agent research pipeline.

        **Pipeline:**
        1. 🔎 Search Agent
        2. 📖 Reader Agent
        3. ✍️ Writer
        4. 🧐 Critic
        """
    )

    st.divider()

    st.caption("Built with LangChain, Mistral AI, Tavily and Streamlit")


# ---------------------------------
# Topic input
# ---------------------------------
st.subheader("Research Topic")

topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Impact of Generative AI on Education"
)


# ---------------------------------
# Run research
# ---------------------------------
if st.button("🚀 Start Research", type="primary"):

    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:

        with st.spinner("AI agents are researching your topic..."):

            try:
                result = run_pipeline(topic)

                st.success("Research completed successfully!")

                # ---------------------------------
                # Search Results
                # ---------------------------------
                st.subheader("🔎 Search Results")

                with st.expander("View search results"):
                    st.write(
                        result.get(
                            "search_results",
                            "No search results available."
                        )
                    )

                # ---------------------------------
                # Scraped Content
                # ---------------------------------
                st.subheader("📖 Retrieved Information")

                with st.expander("View scraped content"):
                    st.write(
                        result.get(
                            "scraped_content",
                            "No scraped content available."
                        )
                    )

                # ---------------------------------
                # Final Report
                # ---------------------------------
                st.subheader("📄 Research Report")

                report = result.get(
                    "report",
                    "No report was generated."
                )

                st.markdown(report)

                # ---------------------------------
                # Critic Report
                # ---------------------------------
                st.subheader("🧐 Critic Review")

                feedback = result.get(
                    "feedback",
                    "No critic feedback was generated."
                )

                st.markdown(feedback)

                # ---------------------------------
                # Download Report
                # ---------------------------------
                st.download_button(
                    label="📥 Download Research Report",
                    data=report,
                    file_name="research_report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error("Something went wrong while running the research pipeline.")

                with st.expander("Error details"):
                    st.exception(e)
