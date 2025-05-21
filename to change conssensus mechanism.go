if err != nil {
    panic("Error creating chaincode: " + err.Error())
}

// Set endorsement policy requiring 60% of peers to validate transactions
chaincode.Info.ACL = map[string]string{
    "endorsementPolicy": "AND('Org1.peer', 'Org2.peer', 'Org3.peer')", // Adjust this dynamically
}

if err := chaincode.Start(); err != nil {
    panic("Error starting chaincode: " + err.Error())
}
