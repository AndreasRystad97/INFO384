// SPDX-License-Identifier: AFL- 3.0
pragma experimental ABIEncoderV2;
pragma solidity 0.6.0;

contract Voting {
    
    struct Candidate {
        uint id;
        string name;
        uint votes;
    }

    mapping (uint => Candidate) private eligable;
    uint public personcount = 0;


    function createCandidate(string memory _name) public{
        eligable[personcount] = Candidate(personcount, _name, 0);
        personcount++;
        
    }

    function voteForCandidate(uint id) public{
        require(id <= personcount);
        eligable[id].votes ++;
    }

    function show_candidates(uint id, string memory name) public view returns (string memory) {
        require(id <= personcount);
        return eligable(name);
    } 
}
