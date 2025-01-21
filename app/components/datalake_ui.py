import gradio as gr
from services.datalake_service import DatalakeService


def datalake_ui():
    datalake_service = DatalakeService()

    async def load_subjects():
        try:
            subjects = await datalake_service.fetch_all_subjects()
            # Ensure subjects is a list of dictionaries with "id" and "name" keys
            return {subject["id"]: subject.get("name", "Unnamed") for subject in subjects}
        except Exception as e:
            return {"error": str(e)}

    async def fetch_studies(subject_id):
        try:
            studies = await datalake_service.fetch_all_studies_by_subject(subject_id)
            # Ensure proper formatting of studies as list of dictionaries
            return [
                {
                    "Study ID": study["id"],
                    "Name": study["name"],
                    "Summary": study.get("summary", ""),
                    "Description": study.get("description", ""),
                    "URL": study.get("url", ""),
                }
                for study in studies
            ]
        except Exception as e:
            return [{"error": str(e)}]

    with gr.Blocks() as datalake_interface:
        gr.Markdown("### Datalake Explorer: Genomic Studies")
        subject_selector = gr.Dropdown(
            label="Select Subject",
            interactive=True,
            multiselect=False,
            choices=[],  # Initially empty, populated later
        )
        study_results = gr.Dataframe(
            headers=["Study ID", "Name", "Summary", "Description", "URL"],
            datatype=["number", "str", "str", "str", "str"],  # Explicit column types
            interactive=False,
        )

        # Button to fetch subjects
        fetch_subjects_btn = gr.Button("Load Subjects")
        fetch_subjects_btn.click(
            fn=load_subjects, inputs=[], outputs=subject_selector, api_name="load_subjects"
        )

        # Subject selection -> Fetch studies
        subject_selector.change(
            fn=fetch_studies, inputs=[subject_selector], outputs=study_results
        )

    return datalake_interface
