from agency_swarm import Agent
from agents.cap_group_agents.VPC_network.cap_agents.VPC_vpc_agent.tools import (
    ReadAPI, GetEndPointAndProjectID
)
from agents.cap_group_agents.cap_agent_instruction import cap_agent_instruction
from agents.basic_agents.job_agent.tools.CallAPI import CallAPI

_name = "VPC_vpc_agent"
_manager_name = "VPC_manager"
_description = """
负责华为云VPC管理任务，包括创建VPC、查询VPC、查询VPC列表、更新VPC、删除VPC。
"""

import os

current_path = os.path.abspath(os.path.dirname(__file__))
_instruction = cap_agent_instruction(_name, _description, _manager_name)


_tools = [ReadAPI.ReadAPI, CallAPI, GetEndPointAndProjectID.GetEndPointAndProjectID]

_file_folder = ""

def create_agent(*, 
                 description=_description, 
                 instuction=_instruction, 
                 tools=_tools, 
                 files_folder=_file_folder):
    return Agent(name=_name,
                 tools=tools,
                 description=description,
                 instructions=instuction,
                 files_folder=_file_folder,
                 temperature=0.5,
                 response_format='auto',
                 max_prompt_tokens=25000,)