from utils.db import database

class DatalakeService:
    """
    Service for interacting with the Datalake database.
    Provides methods to query subjects, studies, and other related data.
    """

    @staticmethod
    async def fetch_all_subjects():
        """
        Fetches all subjects from the 'subjects' table.
        """
        query = "SELECT id, name FROM subjects ORDER BY id ASC"
        rows = await database.fetch_all(query=query)
        return [{"id": row["id"], "name": row["name"]} for row in rows]

    @staticmethod
    async def fetch_studies_by_subject(subject_id: int):
        """
        Fetches studies for a given subject ID.
        """
        query = """
        SELECT study_name, study_summary, study_url
        FROM subject_studies
        WHERE subject_id = :subject_id
        ORDER BY study_name ASC
        """
        rows = await database.fetch_all(query=query, values={"subject_id": subject_id})
        return [{"study_name": row["study_name"], "summary": row["study_summary"], "url": row["study_url"]} for row in rows]
