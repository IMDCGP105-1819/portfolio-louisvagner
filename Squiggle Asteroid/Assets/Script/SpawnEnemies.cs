using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnEnemies : MonoBehaviour {

    public GameObject[] objects;                // The prefab to be spawned.
    public float spawnTime = 2f;            // How long between each spawn.
    private Vector3 spawnPosition;

    // Use this for initialization
    void Start()
    {
        // Call the Spawn function after a delay of the spawnTime and then continue to call after the same amount of time.
        InvokeRepeating("Spawn", spawnTime, spawnTime);

    }

    void Spawn()
    {
        spawnPosition.x = Random.Range(-17, 19);
        spawnPosition.y = 17f;

        Instantiate(objects[UnityEngine.Random.Range(0, objects.Length - 1)], spawnPosition, Quaternion.identity);
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
