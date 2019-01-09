using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour
{
    public GameObject asteroidExplosion;
    public GameObject starshipExplosion;
    public GameObject playerExplosion;

    private int scoreValue;
    private GameController gameController;

    void Start()
    {
        GameObject gameControllerObject = GameObject.FindWithTag("GameController");
        if (gameControllerObject != null)
        {
            gameController = gameControllerObject.GetComponent<GameController>();
        }
        if (gameController == null)
        {
            Debug.Log("Cannot find 'GameController' script");
        }
    }

    //void OnTriggerEnter(Collider other)
    //{
    //if (other.CompareTag("Boundary") || other.CompareTag("Enemy"))
    //{
    //return;
    //}

    //if (asteroidExplosion != null)
    //{
    //Instantiate(asteroidExplosion, transform.position, transform.rotation);
    //}

    //if (other.CompareTag("Player"))
    //{
    //Instantiate(playerExplosion, other.transform.position, other.transform.rotation);
    //gameController.GameOver();
    //}
    //gameController.AddScore(scoreValue);
    //Destroy(other.gameObject);
    //Destroy(gameObject);

    void OnCollisionEnter2D(Collision2D col)
    {
        if (col.gameObject.name == "Asteroids(Clone)")
        {
            Destroy(col.gameObject);
            Instantiate(asteroidExplosion, transform.position, transform.rotation);
            scoreValue = 10;
        }
        else if (col.gameObject.name == "Asteroids (1)(Clone)")
        {
            Destroy(col.gameObject);
            Instantiate(asteroidExplosion, transform.position, transform.rotation);
            scoreValue = 5;
        }
        else if (col.gameObject.name == "Asteroids (2)(Clone)")
        {
            Destroy(col.gameObject);
            Instantiate(asteroidExplosion, transform.position, transform.rotation);
            scoreValue = 10;
        }
        else if (col.gameObject.name == "Starship(Clone)")
        {
            Destroy(col.gameObject);
            Instantiate(starshipExplosion, transform.position, transform.rotation);
            scoreValue = 20;
        }
        else if (col.gameObject.name == "Laser(Clone)")
        {
            Destroy(col.gameObject);
        }

    gameController.AddScore(scoreValue);
    
    }

    //void OnTriggerEnter(Collider col)
    //{
    //Instantiate(playerexplosion, transform.position, transform.rotation);
    //if (col.gameObject.name == "Asteroids")
    //{
    //Destroy(col.gameObject);
    //}
    //}
}

