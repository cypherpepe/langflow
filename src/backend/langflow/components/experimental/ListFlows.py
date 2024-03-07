from typing import List

from langflow import CustomComponent
from langflow.schema import Record


class ListFlowsComponent(CustomComponent):
    display_name = "List Flows"
    description = "A component to list all available flows."
    beta: bool = True

    def build_config(self):
        return {}

    def build(
        self,
    ) -> List[Record]:
        flows = self.list_flows()
        self.status = flows
        return flows
