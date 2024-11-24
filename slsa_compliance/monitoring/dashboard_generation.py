from grafanalib.core import *

dashboard = Dashboard(
    title="SLSA Compliance Dashboard",
    panels=[
        TimeSeries(
            title="Compliance Status",
            dataSource="CSV",
            targets=[
                Target(
                    expr="compliance_status",
                    refId="A",
                ),
            ],
            gridPos=GridPos(h=8, w=12, x=0, y=0),
        ),
        TimeSeries(
            title="Failed Compliance Checks",
            dataSource="CSV",
            targets=[
                Target(
                    expr="failed_checks",
                    refId="B",
                ),
            ],
            gridPos=GridPos(h=8, w=12, x=12, y=0),
        ),
        TimeSeries(
            title="Average Risk Score",
            dataSource="CSV",
            targets=[
                Target(
                    expr="average_risk_score",
                    refId="C",
                ),
            ],
            gridPos=GridPos(h=8, w=12, x=0, y=8),
        ),
    ],
).auto_panel_ids()