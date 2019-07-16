using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Description;
using Crookies.Models;

namespace Crookies.Controllers
{
    public class CrookieController : ApiController
    {
        private SparkthonEntities1 db = new SparkthonEntities1();

        // GET: api/Crookies
        public IQueryable<Crookie> GetCrookie()
        {
            return db.Crookie;
        }

        // GET: api/Crookies/5
        [ResponseType(typeof(Crookie))]
        public IHttpActionResult GetCrookie(int id)
        {
            Crookie crookie = db.Crookie.Find(id);
            if (crookie == null)
            {
                return NotFound();
            }

            return Ok(crookie);
        }

        // PUT: api/Crookies/5
        [ResponseType(typeof(void))]
        public IHttpActionResult PutCrookie(int id, Crookie crookie)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            if (id != crookie.ID)
            {
                return BadRequest();
            }

            db.Entry(crookie).State = EntityState.Modified;

            try
            {
                db.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CrookieExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return StatusCode(HttpStatusCode.NoContent);
        }

        // POST: api/Crookies
        [ResponseType(typeof(Crookie))]
        public IHttpActionResult PostCrookie(Crookie crookie)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            db.Crookie.Add(crookie);
            db.SaveChanges();

            return CreatedAtRoute("DefaultApi", new { id = crookie.ID }, crookie);
        }

        // DELETE: api/Crookies/5
        [ResponseType(typeof(Crookie))]
        public IHttpActionResult DeleteCrookie(int id)
        {
            Crookie crookie = db.Crookie.Find(id);
            if (crookie == null)
            {
                return NotFound();
            }

            db.Crookie.Remove(crookie);
            db.SaveChanges();

            return Ok(crookie);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        private bool CrookieExists(int id)
        {
            return db.Crookie.Count(e => e.ID == id) > 0;
        }
    }
}