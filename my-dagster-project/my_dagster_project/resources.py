from dagster_duckdb import DuckDBResource


duckdb_resource = DuckDBResource(
    database = 'my_dagster_project/database/youtube'
)