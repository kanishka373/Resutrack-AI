import streamlit as st
from supabase import create_client, Client

# Secrets se connection banega
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"] 

supabase: Client = create_client(url, key)

def add_scan(session_id, entry):
    """Saves one analysis result, tagged with the browser session's unique ID."""
    supabase.table("scans").insert({
        "session_id": session_id,
        "date": entry.get("date", ""),
        "timestamp": entry.get("timestamp", ""),
        "role": entry.get("role", ""),
        "filename": entry.get("filename", ""),
        "ats_score": entry.get("ats_score", 0),
        "detected": entry.get("detected", []),
        "missing": entry.get("missing", []),
        "insight": entry.get("insight", "")
    }).execute()

def get_history(session_id):
    """Returns all scans belonging to this session_id only — other sessions' data is never mixed in."""
    response = supabase.table("scans").select("*").eq("session_id", session_id).order("id").execute()
    rows = response.data

    history = []
    for row in rows:
        history.append({
            "db_id": row["id"],
            "date": row["date"],
            "timestamp": row["timestamp"],
            "role": row["role"],
            "filename": row["filename"],
            "ats_score": row["ats_score"],
            "detected": row["detected"] if row["detected"] else [],
            "missing": row["missing"] if row["missing"] else [],
            "insight": row["insight"]
        })
    return history
def delete_scan(db_id):
    """Deletes a single scan by its database ID."""
    supabase.table("scans").delete().eq("id", db_id).execute()
